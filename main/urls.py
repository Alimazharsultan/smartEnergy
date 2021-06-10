from django.urls import path
from .import views

urlpatterns = [

    
    path("<int:id>", views.index2, name="Dynamic Page"),
    
    path("login/", views.loginpage, name="login"),
    path("register/", views.registerpage, name="register"),
    path("logout/", views.logoutuser, name="logout"),

    path("values/", views.valuess, name="values"),
    path("sensor/", views.sensors, name="sensors"),
    path("", views.home, name="home"),
    path("site1/", views.site1, name="site1"),
    path("site2/", views.site2, name="site2"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="create"),
]