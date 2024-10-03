from.import views
from django.urls import path
from django.contrib.auth.views import LoginView
urlpatterns=[
    path('',views.index),
    path('about/',views.aboutview),
    path('register/',views.register_view,name='register'),
    path('login',LoginView.as_view(template_name='login.html'),name='Login'),
]
