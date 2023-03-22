from django.db import models
from django.contrib.auth.models import AbstractUser
import random

memes = [
    'https://www.goodwill.ab.ca/wp-content/uploads/2018/04/happy-the-office-GIF-downsized.gif',
    'https://thumbs.gfycat.com/SinfulElaborateBarasingha-max-1mb.gif',
    'https://www.magiquiz.com/wp-content/uploads/2017/10/giphy3.gif',
    'https://j.gifs.com/zKxZPy.gif',
    'https://www.theknot.com/tk-media/images/1ee35569-83cc-4939-b510-fa12d8fe41c0~rs_768.h'
]


# class Answer(models.Model):
#     name = models.CharField(max_length=20)
#     photo = models.ImageField(null=True)
#     correct = models.BooleanField(null=True, default=False)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class Exam(models.Model):
#     name = 'Exam'
#     task = models.CharField(max_length=200)
#     answers = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class Explonation(models.Model):
#     name = "Explonation"
#     video_explonation = models.URLField(null=True)
#     audio_explonation = models.URLField(null=True, default=video_explonation)
#     text_explonation = models.TextField()
#     kinetic_explonation = models.URLField(null=True, default=video_explonation)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class Bootcamp(models.Model):
#     name = "Bootcamp"
#     task = models.CharField(max_length=250)
#     trials = models.IntegerField(default=0)
#     case_check = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     case_explonation = models.ForeignKey(Explonation, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class Topic(models.Model):
#     name = models.CharField(max_length=20)
#     meme = models.TextField(null=True, blank=True, default=random.choice(memes))
#     description = models.CharField(max_length=300, null=True)
#     explonation = models.ForeignKey(Explonation, on_delete=models.CASCADE, null=True)
#     bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, null=True)
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class Course(models.Model):
#     name = models.CharField(max_length=20)
#     photo = models.ImageField(null=True, default="graduation-cap.svg")
#     courses = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
#     description = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class Classes(models.Model):
#     name = models.CharField(max_length=20)
#     photo = models.ImageField(null=True, default="graduation-cap.svg")
#     gif = models.URLField(null=True)
#     courses = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
#     description = models.TextField(max_length=300, null=True, blank=True)
#
#     def __str__(self):
#         return str(self.name)


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50, null=True)
    username = models.CharField(unique=True, max_length=200, null=True)
    email = models.EmailField(unique=True)

    avatar = models.ImageField(null=True, default="user.png")
    # classes = models.ForeignKey(
    #     Classes,
    #     on_delete=models.CASCADE,
    #     null=True
    # )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
