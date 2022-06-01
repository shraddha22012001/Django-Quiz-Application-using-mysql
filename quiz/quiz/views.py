from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context
from quiz.models import Exam
from quiz.forms import QuestionForm
from django.contrib import messages


def home(request):
    return render(request,"home.html")

def quiz(request):
    questions = Exam.objects.all()  
    return render(request,"quiz.html",{'questions':questions}) 

 
def index(request):
 
    item_list = Exam.objects.order_by("Question")
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = QuestionForm()
 
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "TODO LIST",
           }
    return render(request, 'index.html', page)
 
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Exam.objects.get(ID=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('index')

def update(request, item_id):
    # fetch the object related to passed id
    obj =Exam.objects.get(ID=item_id)

 
    # pass the object as instance in form
    form = QuestionForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('index')
 
    return render(request, "update.html",{'obj':obj})

