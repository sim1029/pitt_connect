from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Class(models.Model):
    department = models.CharField(max_length=8)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=50)

    SPRING = "SP"
    SUMMER = "SM"
    FALL = "FL"

    TERM_CHOICES = [
        (SPRING, "Spring"),
        (SUMMER, "Summer"),
        (FALL, "Fall"),
    ]

    term = models.CharField(
        max_length = 2,
        choices = TERM_CHOICES,
    )

    year = models.IntegerField(default=2021)

    # MON = "MON"
    # TUE = "TUE"
    # WED = "WED"
    # THU = "THU"
    # FRI = "FRI"
    #
    # DAY_CHOICES = [
    #     (MON, "Monday"),
    #     (TUE, "Tueday"),
    #     (WED, "Wednesday"),
    #     (THU, "Thursday"),
    #     (FRI, "Friday"),
    # ]

    lecture_days = models.CharField(max_length = 30)

    lecture_time = models.CharField(max_length=100)

    recitation_days = models.CharField(max_length = 30,blank=True)

    recitation_time = models.CharField(max_length=100,blank=True)

    office_days = models.CharField(max_length = 30,blank=True)

    office_time = models.CharField(max_length=100,blank=True)

    zoom = models.CharField(max_length=300,blank=True)
    discord = models.CharField(max_length=300,blank=True)
    slack = models.CharField(max_length=300,blank=True)
    groupme = models.CharField(max_length=300,blank=True)
    tophat = models.CharField(max_length=300,blank=True)
    canvas = models.CharField(max_length=300,blank=True)
    gradescope = models.CharField(max_length=300,blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # string with comma separated list of class ids
    classes = models.CharField(max_length=30,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
