from django.urls import path 
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login/",views.login_,name="login"),
    path("logout/",views.logout_,name="logout"),

]