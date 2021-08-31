from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]

    info = {
        'name' : 'minchae'
    }

    context = {
        'info' : info,
        'foods' : foods,
    }

    return render(request, 'greeting.html', context)

def dinner(request):
    foods = ['hamburger', 'chicken', 'rolls']
    pick = random.choice(foods)
    no = ''

    context = {
        'pick': pick,
        'foods': foods,
        'no': no,
    }
    return render(request, 'dinner.html', context)

def image(request):

    return render(request, 'image.html')

def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'mango', 'coconut']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }

    return render(request, 'template_language.html', context)


def throw(request):

    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)