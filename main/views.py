from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Class

# Create your views here.

def index(request):
    context = {
        'classes' : Class.objects.all(),
    }
    return render(request, 'main/index.html', context)

def search(request):
    return render(request, 'main/class_search.html', {})

def login(request):
    return render(request, 'main/login.html', {})

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
    }

    return render(request, 'main/class.html', context)
