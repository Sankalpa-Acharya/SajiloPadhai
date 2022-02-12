from django.urls import path
from . import views

urlpatterns=[

    path('',views.HomeView.as_view()),
    path('courses',views.CourseView.as_view()),
    path('video/<slug:slug>',views.VideoView.as_view()),
    path('login',views.LoginView.as_view(), name='login'),
    path('singup',views.SingUpView.as_view(), name='singup'),
]