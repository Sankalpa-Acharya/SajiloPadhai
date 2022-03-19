from django.urls import path
from django.contrib.auth import views as auth_views     
from . import views
urlpatterns=[

    path('',views.HomeView.as_view()),
    path('course/<slug:slug>',views.CourseView.as_view(),name='course'),
    path('video/<slug:slug>',views.VideoView.as_view(),name='video'),
    path('allcourses',views.AllCourse,name='all course'),


    path('accounts/login/',views.LoginView.as_view(), name='login'),
    path('accounts/singup',views.SingUpView.as_view(), name='singup'),


    # password reset section    
     path('reset_password/',auth_views.PasswordResetView.as_view(template_name='courses/password_reset.html'),name='reset_password'),

     path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='courses/password_reset_done.html'),name='password_reset_done' ),

     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='courses/reset_token.html'),name='password_reset_confirm'),

     path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='courses/reset_complete.html'),name='password_reset_complete'),

]