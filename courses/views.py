from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import SingUpForm
from .models import Course,Video
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.





class HomeView(View):
    def get(self,request):
        all_course=Course.objects.all()[:3]
        context={'courses':all_course}
        return render(request,'courses/index.html',context)




class CourseView(View):
    def get(self,request,slug):
        course=Course.objects.get(slug=slug)
        try:
            video=Video.objects.filter(course=course).reverse()[0]
            slug_value=video.slug
        except:
            return HttpResponseRedirect('/')
            
        return HttpResponseRedirect(f'/video/{slug_value}')



@login_required(login_url='/accounts/login')
def AllCourse(request):
    allvideo=Course.objects.all()
    context={
        'all':allvideo,
    }
    return render(request,'courses/courses.html',context)



class VideoView(View):
    @method_decorator(login_required)
    def get(self,request,slug):

      
        CourseVideo = Video.objects.get(slug=slug)
        # course_info =Course.objects.get(name=CourseVideo.course) 
        AllVideo = Video.objects.filter(course=CourseVideo.course)
        
        context={'video':CourseVideo,'all':AllVideo}
        return render(request,'courses/content.html',context)
    
  




class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/allcourses')
        form=AuthenticationForm()
        context={'form':form}
        return render(request,'courses/login.html',context)

    def post(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/allcourses')
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            print('this is ok')
            uname=request.POST['username']
            upass=request.POST['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/allcourses')
        else:
            messages.error(request,'Invalid Email or Password')
        context={'form':form}
        return render(request,'courses/login.html',context)





class SingUpView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/allcourses')
        form=SingUpForm()
        context={'form':form}
        return render(request,'courses/singup.html',context)

    def post(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/allcourses')
        form=SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Account Has Been Created , Now Login')
        context={'form':form}
        return render(request,'courses/singup.html',context)




