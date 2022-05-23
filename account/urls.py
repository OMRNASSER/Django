from django.urls import path , include 

from . import views 


urlpatterns = [
    path('signup.html',views.register_request , name= "signup"),
    path('login.html', views.login_request, name ='login')
    

]