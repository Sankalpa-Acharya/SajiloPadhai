from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[

    path('',views.HomeView.as_view()),
    path('course/<slug:slug>',views.CourseView.as_view(),name='course'),
    path('video/<slug:slug>',views.VideoView.as_view(),name='video'),
    path('allcourses',views.AllCourse),


    path('login',views.LoginView.as_view(), name='login'),
    path('singup',views.SingUpView.as_view(), name='singup')
]