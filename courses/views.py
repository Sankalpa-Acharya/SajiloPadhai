from django.shortcuts import render
from django.views import View
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
        return render(request,'courses/login.html')




class SingUpView(View):
    def get(self,request):
        return render(request,'courses/singup.html')




