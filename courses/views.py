from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import SingUpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

class HomeView(View):
    def get(self,request):
        return render(request,'courses/index.html')


class CourseView(View):
    def get(self,request):
        return render(request,'courses/courses.html')




class VideoView(View):
    def get(self,request,slug):
        return render(request,'courses/content.html')




class LoginView(View):
    def get(self,request):
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'courses/login.html',context)

    def post(self,request):
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname=request.POST['username']
            upass=request.POST['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/courses')
        context={'form':form}
        return render(request,'courses/login.html',context)





class SingUpView(View):
    def get(self,request):
        form=SingUpForm()
        context={'form':form}
        return render(request,'courses/singup.html',context)

    def post(self,request):
        form=SingUpForm(request.POST)
        if form.is_valid():
            form.save()
        context={'form':form}
        return render(request,'courses/singup.html',context)




