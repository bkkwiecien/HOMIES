from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User
    # , Classes, Course, Topic, Explonation, Bootcamp, Exam, Answer
from .forms import MyUserCreationForm
from django.contrib import messages


data= {
    "user_photo": './media/olivia.jpeg',
    "username": "olivia",
    "user_first_name": "Olivia",
    "user_second_name": 'Rodrigo',
    "user_email": 'oliviarodrigo@gmail.com',
    "classes": [
        {
            "class_name": "MATHEMATICS",
            "class_icon": './media/divide.png',
            "class_gif": 'https://media.tenor.com/q_AusGzukP8AAAAd/math-equations-math-meme.gif',
            "class_description": 'just a math class',
            "class_content": {
                "previous_lesson": {
                        "lesson_name": "DERIVATIVES",
                        "lesson_number": "4.2",
                        "lesson_description": "Partial derivatives is a method to calculate the derivative of a function with respect to one or more variables. It is also called as partial differentiation.",
                        "progres": 85
                    },
                "lessons": [
                    {
                        "lesson_name": "PARTIAL DERIVARIVES",
                        "lesson_number": "4.3",
                        "progres": 0
                    }, {
                        "lesson_name": "DERIVATIVES EXAM",
                        "lesson_number": "4.4",
                        "progres": 0
                    }, {
                        "lesson_name": "GEOMETRY INTRO",
                        "lesson_number": "5.0",
                        "progres": 0
                    }, {
                        "lesson_name": "2D GEOMETRY",
                        "lesson_number": "5.1",
                        "progres": 0
                    }, {
                        "lesson_name": "SPATIAL GEOMETRY",
                        "lesson_number": "5.2",
                        "progres": 0
                    }]
            }
        },
        {
            "class_name": "PHYSICS",
            "class_icon": './media/nuclear-bomb.png',
            "class_gif": 'https://thumbs.gfycat.com/AnnualMeaslyEnglishpointer-size_restricted.gif',
            "class_content": {
                "previous_lesson": {
                        "lesson_name": "BLACK HOLES",
                        "lesson_number": "10.4",
                        "lesson_description": "In this lesson, students will learn about the formation, properties, and behavior of black holes, as well as their impact on our understanding of the universe.",
                        "progres": 40
                    },
                "lessons": [
                    {
                        "lesson_name": "GRAVITY ANOMALIES",
                        "lesson_number": "10.5",
                        "progres": 0
                    }, {
                        "lesson_name": "TIME ANOMALY",
                        "lesson_number": "10.6",
                        "progres": 0
                    }, {
                        "lesson_name": "INTERSTELLAR",
                        "lesson_number": "10.7",
                        "progres": 0
                    }, {
                        "lesson_name": "EXAM",
                        "lesson_number": "10.8",
                        "progres": 0
                    }]
            }
        },
        {
            "class_name": "CHEMISTRY",
            "class_icon": './media/test-tube.png',
            "class_gif": 'https://media.tenor.com/cBuVdl0HryMAAAAC/walter-white-breaking-bad.gif',
            "class_content": {
                "previous_lesson": {
                        "lesson_name": "CRISTALS",
                        "lesson_number": "4.0",
                        "lesson_description": "In this lesson, students will learn about the effects, risks, and consequences of methamphetamine use, as well as the resources available for addiction treatment and recovery.",
                        "progres": 100
                    },
                "lessons": [
                    {
                        "lesson_name": "STEREOIDS",
                        "lesson_number": "4.1",
                        "progres": 0
                    }, {
                        "lesson_name": "DRUGS",
                        "lesson_number": "4.2.0",
                        "progres": 0
                    }, {
                        "lesson_name": "PRACTISE EXAM",
                        "lesson_number": "4.3",
                        "progres": 0
                    }, {
                        "lesson_name": "EXAM",
                        "lesson_number": "4.4",
                        "progres": 0
                    }]
            }
        },
        {
            "class_name": "GEOGRAPHY",
            "class_icon": './media/globe.png',
            "class_gif": 'https://media.tenor.com/t-LFiq203l8AAAAd/kim-jongun-hi.gif',
            "class_content": {
                "previous_lesson": {
                        "lesson_name": "NORTH KOREA",
                        "lesson_number": "2.1",
                        "lesson_description": "In this lesson, students will learn about the history, politics, and society of North Korea, including its nuclear program and international relations with other countries.",
                        "progres": 55
                    },
                "lessons": [
                    {
                        "lesson_name": "RUSSIA",
                        "lesson_number": "2.2",
                        "progres": 0
                    }, {
                        "lesson_name": "CHINA",
                        "lesson_number": "2.3",
                        "progres": 0
                    }, {
                        "lesson_name": "UNITED STATES",
                        "lesson_number": "2.4",
                        "progres": 0
                    }, {
                        "lesson_name": "WEST ASIA",
                        "lesson_number": "2.5",
                        "progres": 0
                    }, {
                        "lesson_name": "GREAT BRITAIN",
                        "lesson_number": "2.6",
                        "progres": 0
                    }]
            }
        },
        {
            "class_name": "POLISH",
            "class_icon": './media/poland.png',
            "class_gif": 'https://64.media.tumblr.com/0c3a60a4d4d927545d184a5edbf40ad2/tumblr_osfms1wvm41w4wz1ko4_400.gifv',
            "class_content": {
                "previous_lesson": {
                        "lesson_name": "PAN TADEUSZ",
                        "lesson_number": "0.1",
                        "lesson_description": 'In this lesson, students will explore the themes, characters, and historical context of the classic Polish epic poem "Pan Tadeusz" by Adam Mickiewicz.',
                        "progres": 95
                    },
                "lessons": [
                    {
                        "lesson_name": "CIERPIENIA MŁODEGO WERTERA",
                        "lesson_number": "0.2",
                        "progres": 0
                    }, {
                        "lesson_name": "DZIADY CZĘŚĆ II",
                        "lesson_number": "0.3",
                        "progres": 0
                    }, {
                        "lesson_name": "DZIADY CZĘŚĆ III",
                        "lesson_number": "0.4",
                        "progres": 0
                    }, {
                        "lesson_name": "DZIADY CZĘŚĆ IV",
                        "lesson_number": "0.5",
                        "progres": 0
                    }, {
                        "lesson_name": "LALKA",
                        "lesson_number": "0.6",
                        "progres": 0
                    }]
            }
        },
        {
            "class_name": "SEX EDUCATION",
            "class_icon": './media/sex.png',
            # "class_gif": 'https://dl.phncdn.com/pics/gifs/026/872/461/(m=ldpwiqacxtE_Ai)(mh=xsDSNrdYGBXX3_u7)26872461b.gif',
            "class_gif": "https://media.tenor.com/-nt9Dj8Ei14AAAAd/tap-that.gif",
            "class_content": {
                "previous_lesson": {
                        "lesson_name": "FOREPLAY",
                        "lesson_number": "6.9",
                        "lesson_description": "n this lesson, students will learn about the importance of foreplay in sexual activity, the different types of foreplay, and how to communicate their preferences with their partner.",
                        "progres": 69
                    },
                "lessons": [
                    {
                        "lesson_name": "SAFE SEX",
                        "lesson_number": "6.10",
                        "progres": 0
                    }, {
                        "lesson_name": "ORAL/BLOWJOB",
                        "lesson_number": "6.11",
                        "progres": 0
                    }, {
                        "lesson_name": "BEST SEX POSES",
                        "lesson_number": "6.12",
                        "progres": 0
                    }, {
                        "lesson_name": "HARD SEX/BDSM",
                        "lesson_number": "6.13",
                        "progres": 0
                    }, {
                        "lesson_name": "MASTURBATION",
                        "lesson_number": "6.14",
                        "progres": 0
                    }]
            }
        }
    ]
}


def success(request):
    return render(request, 'success.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)

        try:
            email = User.objects.get(email=email)
            print(email)
            print(password)
            user = authenticate(username='bkkwiecien', password='Pold3e123')
            print(user)
            if user is not None:
                login(request, user)
                print('redurecting')
                return redirect('home')
            else:
                messages.error(request, 'Wrong username OR password')
        except:
            messages.error(request, 'User does not exist')

    return render(request, 'login.html', {})


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    if request.method == 'POST':
        first = request.POST.get('first_name')
        second = request.POST.get('second_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        # confirm_password = request.POST.get('password2')

        print(first)
        print(second)
        print(username)
        print(email)
        print(password)
        # print(confirm_password)
        user = User(first_name=first,
                    second_name=second,
                    username=username,
                    email=email,
                    password=password)

        user.save()
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, "An error occurred during registration")

    return render(request, 'register.html', {})


def homeBoard(request):
    # if not request.user.is_authenticated:
    #     return redirect('sign-in')
    context = {'data': data, 'user': request.user}
    return render(request, 'home_board.html', context)


def classBoard(request, pk):
    hover_class = None
    for course in data['classes']:
        if course['class_name'] == pk:
            hover_class = course

    context = {'data': data,
               'hover_class': hover_class}

    return render(request, 'class_board.html', context)


def addBoard(request):
    context = {'data': data}
    return render(request, 'add_board.html', context)


def userBoard(request):
    context = {'data': data}
    return render(request, 'add_board.html', context)
