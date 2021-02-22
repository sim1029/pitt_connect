from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .models import Class

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        classes = []
        for class_id in request.user.profile.classes.split(','):
            if class_id:
                classes.append(Class.objects.get(pk=int(class_id)))

        context = { 'classes' : classes }
        return render(request, 'app/index.html', context)
    else:
        return render(request, 'app/welcome.html', {})

def search(request):
    if not request.user.is_authenticated:
        return redirect('login')

    user_classes = []
    for i in request.user.profile.classes.split(','):
        if i:
            user_classes.append(int(i))

    if request.method == "POST":
        # empty search

        if not request.POST['search']:
            context = {
                'classes': Class.objects.all(),
                'user_classes': user_classes,
                'error': "Empty search."
            }
            return render(request, 'app/class_search.html', context)

        department = ""
        code = ""

        cnum = request.POST['search']
        while cnum != "":
            if cnum.isdigit():
                code = cnum.strip()
                break
            elif cnum.isspace():
                continue
            else:
                department += cnum[0]
                cnum = cnum[1:]

        classes = None
        if department:
            classes = Class.objects.filter(department=department)

        if classes and code:
            classes = classes.filter(code=code)
        elif code:
            classes = Class.objects.filter(code=code)

        if classes:
            context = {
                'classes': classes,
                'user_classes': user_classes,
                'error': ""
            }
            return render(request, 'app/class_search.html', context)
        else:
            context = {
                'classes': Class.objects.all(),
                'user_classes': user_classes,
                'error': "No results found."
            }
            return render(request, 'app/class_search.html', context)

    else:
        context = {
            'classes' : Class.objects.all(),
            'user_classes': user_classes,
            'error': ""
        }
        return render(request, 'app/class_search.html', context)

def add(request, class_id):
    if request.user.is_authenticated:
        classes = request.user.profile.classes
        # don't duplicate a class in the user
        if str(class_id) not in classes:
            classes += ',' + str(class_id)

            request.user.profile.classes = classes
            request.user.save()

        n = request.POST.get('next', '/')
        return redirect(n)
    else:
        return redirect('login')

def remove(request, class_id):
    if request.user.is_authenticated:
        classes = request.user.profile.classes

        if str(class_id) in classes:
            # remove class
            new_classes = ""
            for c in classes.split(','):
                if c != str(class_id):
                    new_classes += c + ','

            # cut off trailing comma
            new_classes = new_classes[:-1]
            request.user.profile.classes = new_classes
            request.user.save()

        n = request.POST.get('next', '/')
        return redirect(n)
    else:
        return redirect('login')

def logout(request):
    auth_logout(request)

    return redirect('index')

def login(request):
    # if user is logged in already, redirect them
    if request.user.is_authenticated:
            return redirect('index')

    if request.method == 'POST':
        # user = User.objects.create_user(
        #     request.POST['uname'],
        #     email=None,
        #     password=request.POST['psw'],
        # )
        #
        # user.save()

        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            context = {
                'error' : True,
            }
            return render(request, 'app/login.html', context)
    else:
        context = {
            'error' : False,
        }
        return render(request, 'app/login.html', context)

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        if request.POST['password'] != request.POST['passwordConfirm']:
            context = { 'error' : "Passwords do not match." }
            return render(request, 'app/sign_up.html', context)
        elif User.objects.filter(username=request.POST['username']).exists():
            context = { 'error' : "Username already taken." }
            return render(request, 'app/sign_up.html', context)
        elif User.objects.filter(email=request.POST['email']).exists():
            context = { 'error' : "Email already taken." }
            return render(request, 'app/sign_up.html', context)
        else:
            user = User.objects.create_user(
                request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
            )

            user.save()

            return redirect('login')
    else:
        context = { 'error' : "" }
        return render(request, 'app/sign_up.html', context)

def create(request):
    if request.method == 'POST':
        department = ""
        code = ""

        cnum = request.POST['courseNum']
        while cnum != "":
            if cnum.isdigit():
                code = cnum
                break
            else:
                department += cnum[0]
                cnum = cnum[1:]

        name = request.POST['courseName']
        instructor = "{0} {1}".format(request.POST['firstName'], request.POST['lastName'])

        [term, year] = request.POST['term'].split(" ")
        if term == "Spring":
            term = "SP"
        elif term == "Summer":
            term = "SM"
        else:
            term = "FL"

        lecday1 = request.POST['lecDay1']
        lecday2 = request.POST['lecDay2']
        lecday3 = request.POST['lecDay3']
        lecture_days = "{0}{1}{2}".format(
            lecday1 if not lecday1.startswith('Day') else "",
            lecday2 if not lecday2.startswith('Day') else "",
            lecday3 if not lecday3.startswith('Day') else "",
        )

        recday1 = request.POST['recDay1']
        recday2 = request.POST['recDay2']
        recitation_days = "{0}{1}".format(
            recday1 if not recday1.startswith('Day') else "",
            recday2 if not recday2.startswith('Day') else "",
        )

        office_days = request.POST['officeDay']

        lecture_time = request.POST['lectureTime']
        recitation_time = request.POST['recitationTime']
        office_time = request.POST['officeTime']

        lecture_link = request.POST['lectureLink']
        recitation_link = request.POST['recitationLink']
        office_link = request.POST['officeLink']

        lecture_pass = request.POST['lecPassword']
        recitation_pass = request.POST['recPassword']
        office_pass = request.POST['officePassword']

        zoom = "{0},{1};{2},{3};{4},{5}".format(
            lecture_link,
            lecture_pass,
            recitation_link,
            recitation_pass,
            office_link,
            office_pass
        )

        discord = request.POST['discordLink']
        groupme = request.POST['groupmeLink']
        slack = request.POST['slackLink']
        tophat = request.POST['tophatLink']
        canvas = request.POST['canvasLink']
        gradescope = request.POST['gradescopeLink']
        box = request.POST['boxLink']
        website = request.POST['websiteLink']

        new_class = Class(
            department=department,
            code=code,
            name=name,
            instructor=instructor,
            term=term,
            year=year,
            lecture_days=lecture_days,
            lecture_time=lecture_time,
            recitation_days=recitation_days,
            recitation_time=recitation_time,
            office_days=office_days,
            office_time=office_time,
            zoom=zoom,
            discord=discord,
            slack=slack,
            groupme=groupme,
            tophat=tophat,
            canvas=canvas,
            gradescope=gradescope,
            box=box,
            website=website
        )

        new_class.save()

        return redirect('index')
    else:
        return render(request, 'app/class_form.html', {})

def class_page(request, class_id):
    c = get_object_or_404(Class, pk=class_id)
    name = c.name

    zoom = False
    lecture = "{0} {1}".format(c.lecture_days, c.lecture_time)
    recitation = "{0} {1}".format(c.recitation_days, c.recitation_time)
    office = "{0} {1}".format(c.office_days, c.office_time)

    lecture_link = ""
    recitation_link = ""
    office_link = ""
    lecture_pass = ""
    recitation_pass = ""
    office_pass = ""
    if c.zoom:
        zoom = True
        parts = c.zoom.split(';')
        for i, part in enumerate(parts):
            [link, password] = part.split(',')
            if i == 0:
                lecture_link = link
                lecture_pass = password
            elif i == 1:
                recitation_link = link
                recitation_pass = password
            else:
                office_link = link
                office_pass = password

    discord = False
    discord_link = ""
    if c.discord:
        discord = True
        discord_link = c.discord

    groupme = False
    groupme_link = ""
    if c.groupme:
        groupme = True
        groupme_link = c.groupme

    slack = False
    slack_link = ""
    if c.slack:
        slack = True
        slack_link = c.slack

    tophat = False
    tophat_link = ""
    if c.tophat:
        tophat = True
        tophat_link = c.tophat

    canvas = False
    canvas_link = ""
    if c.canvas:
        canvas = True
        canvas_link = c.canvas

    gradescope = False
    gradescope_link = ""
    if c.gradescope:
        gradescope = True
        gradescope_link = c.gradescope

    box = False
    box_link = ""
    if c.box:
        box = True
        box_link = c.box

    website = False
    website_link = ""
    if c.website:
        website = True
        website_link = c.website

    context = {
        'name' : name,
        'zoom' : zoom,
        'lecture' : lecture,
        'recitation' : recitation,
        'office' : office,
        'lecture_link' : lecture_link,
        'recitation_link' : recitation_link,
        'office_link' : office_link,
        'lecture_pass' : lecture_pass,
        'recitation_pass' : recitation_pass,
        'office_pass' : office_pass,
        'discord' : discord,
        'discord_link' : discord_link,
        'groupme' : groupme,
        'groupme_link' : groupme_link,
        'slack' : slack,
        'slack_link' : slack_link,
        'tophat' : tophat,
        'tophat_link' : tophat_link,
        'canvas' : canvas,
        'canvas_link' : canvas_link,
        'gradescope' : gradescope,
        'gradescope_link' : gradescope_link,
        'box' : box,
        'box_link' : box_link,
        'website' : website,
        'website_link' : website_link,
    }

    return render(request, 'app/class.html', context)
