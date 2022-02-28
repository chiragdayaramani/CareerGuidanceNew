from contextlib import redirect_stderr
from itertools import count
from turtle import color
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Result10Count, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.models import After10, After12Arts, After12Commerce, After12Science ,After10colleges, After12engcolleges, After12medicolleges,After12commcolleges,After12artscolleges,result,result12arts,result12comm,result12sci
from .forms import SignUpForm, LoginForm
from django.db.models.query_utils import DeferredAttribute
import random
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression

# Create your views here.

def home(request):
    count=User.objects.count()
    context={
        'count':count,
    }
    return render(request,'home.html',context)

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data.get("email")
            password= form.cleaned_data.get("password")
            try:
                user= User.objects.get(email=email, password=password)
                print(user.email)
                print(user.password)
                messages.info(request, "You are now logged in as {user.email}.")
                # messages.INFO(request, f"You are now logged in as {email}.")
                return redirect("home")
            except User.DoesNotExist:
                print("Invalid user!!")
        messages.error(request,"Invalid username or password.")
        return redirect('signup')
    else:
        print("method != POST")
        form=  LoginForm()
        context = {
            'form':form,

        }
        return render(request, 'registration/login.html', context)
    
def signup(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form=  SignUpForm()
    context = {
        'form':form,
    }
    return render(request,'registration/signup.html',context)

def get_questions():
    questions=After10.objects.all();
    return questions
def after10(request):
    questions=After10.objects.all();
    # for question in questions:
    #     print(question.id);
    context={
        'questions':questions
    }
    return render(request, 'after10.html',context)
def after10result(request):
    if request.method == "POST":
        flag=False
        questions=get_questions();
        form=request.POST.get("after10form")
        username = User.email
        sc = 0
        ac = 0
        cc = 0
        dc = 0
        # questions = list(questions)
        # random.shuffle(questions)
        results = pd.DataFrame()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=file.csv'
        results.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
        writer = csv.writer(response)  
        writer.writerow(['question', 'answer', 'username', 'question_type','marks'])
        # x = []
        # y = []
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            type=question.question_type
            print(q_id, option_selected,type)
            # correct_ans=question.correct_answer
            # print(correct_ans)
            print(question.correct_answer == option_selected)
            if(q_id != None and option_selected!= None):
                ans = result(question = q_id,answer = option_selected,username = username,question_type=type, )
                option_selected=(option_selected)
                writer.writerow([q_id, option_selected, username, type,question.correct_answer == option_selected])
                # x.append(q_id)
                # y.append(question.correct_answer == option_selected)
                if (question.correct_answer == option_selected and type == 'C'):
                    cc = cc+1
                elif (question.correct_answer == option_selected and type == 'A'):
                    ac = ac+1
                elif (question.correct_answer == option_selected and type == 'S'):
                    sc = sc+1
                elif (question.correct_answer == option_selected and type == 'D'):
                    dc = dc+1
                ans.save()
                flag=True
        # email= form.cleaned_data.get("email")
        # password= form.cleaned_data.get("password")
        # user= User.objects.get(email=email, password=password)
        # print(user.email)
        # print(user.password)
        countResult=Result10Count(username=username,count_science=sc,count_arts=ac,count_commerce=cc,count_diploma=dc)   
        countResult.save()
        total = sc + ac + cc + dc
        perS = int((sc/total) * 100)
        perA = int((ac/total) * 100)
        perC = int((cc/total) * 100)
        perD = int((dc/total) * 100)
        print(ac,cc,sc,dc)
        res = max(ac,cc,sc,dc)
        print(username)
        print(User.email) 
        # print(x)
        # print(y)
        # foo = response.content.decode('utf-8')
        type = ["Science","Commerce","Arts","Diploma"]
        marks = [sc, cc, ac, dc]
        # plt.bar(type, marks, color = ["#00fff8","#41b6be","#0c95f3","#275cd8"], width = 0.5)
        plt.bar(type, marks, color = ["#7594f3","#2557ed",  "#00ecff","#092169"], width = 0.5)
        plt.title("SCORE CARD!")
        plt.xlabel("Stream")
        plt.ylabel("Marks")
        plt.show()
           
    return render(request, "after10result.html", {'flag': flag,'sc':sc,'cc':cc,'ac':ac,'dc':dc, 'res' : res,'total':total,'perS':perS,'perA':perA,'perC':perC,'perD':perD, })
    # response = response.iloc[1:]
    return response
    


def get_questions12arts():
    questions=After12Arts.objects.all();
    return questions
def after12arts(request):
    questions=After12Arts.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12arts.html',context)
def after12artsresult(request):
    if request.method == "POST":
        flag=False
        questions=get_questions12arts();
        form=request.POST.get("after12form")
        username = User.email
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            print(q_id, option_selected)
            if(q_id != None and option_selected!= None):
                ans = result12arts(question = q_id,answer = option_selected,username = username )
                ans.save()
                flag=True   
        print(username)      
    return render(request, "after12artsresult.html", {'flag': flag})
    
def get_questions12comm():
    questions=After12Commerce.objects.all();
    return questions
def after12commerce(request):
    questions=After12Commerce.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12comm.html',context)
def after12commresult(request):
    if request.method == "POST":
        flag=False
        questions=get_questions12comm();
        form=request.POST.get("after12form")
        username = User.email
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            print(q_id, option_selected)
            if(q_id != None and option_selected!= None):
                ans = result12comm(question = q_id,answer = option_selected,username = username )
                ans.save()
                flag=True   
        print(username)      
    return render(request, "after12commresult.html", {'flag': flag})
    
def get_questions12sci():
    questions=After12Science.objects.all();
    return questions
def after12science(request):
    questions=After12Science.objects.all()
    context={
        'questions':questions
    }
    return render(request, 'after12sci.html',context)
def after12sciresult(request):
    if request.method == "POST":
        flag=False
        questions=get_questions12sci();
        form=request.POST.get("after12form")
        username = User.email
        for question in questions:
            #print(question.id)
            # user_id = result.objects.get(user_id = user_id)
            # ip = User.objects.get() # query the InsertIp object
            # user = User.user # get the user using a . operator
            q_id=question.id
            option_selected=request.POST.get(str(q_id))
            print(q_id, option_selected)
            if(q_id != None and option_selected!= None):
                ans = result12sci(question = q_id,answer = option_selected,username = username )
                ans.save()
                flag=True   
        print(username)      
    return render(request, "after12sciresult.html", {'flag': flag})
    
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def feedbackform(request):
    return render(request,"feedbackform.html")

def logout(request):
    messages.info(request, "You have successfully logged out.") 
    redirect("login")
  
def after10colleges(request):
    colleges = After10colleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after10colleges.html',context)
def after12engcolleges(request):
    colleges = After12engcolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12engcolleges.html',context)
def after12medicolleges(request):
    colleges = After12medicolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12medicolleges.html',context)
def after12commcolleges(request):
    colleges = After12commcolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12commcolleges.html',context)
def after12artscolleges(request):
    colleges = After12artscolleges.objects.all()
    context={
        'colleges':colleges
    }
    return render(request, 'after12artscolleges.html',context)

