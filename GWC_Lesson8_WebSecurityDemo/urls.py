"""
URL configuration for GWC_Lesson8_WebSecurityDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView
from WebSecurity.views import home_view
from WebSecurity.views import amaze_view
from WebSecurity.views import barbie_view
from WebSecurity.views import barbie_flag
from WebSecurity.views import notebook_view
from WebSecurity.views import fallguy_view
from WebSecurity.views import login_view
from WebSecurity.views import lala_view

urlpatterns = [
    path("", home_view, name="home"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("amaze_amaze_amaze", amaze_view, name="amaze"),
    path("barbie", barbie_view, name="barbie"),
    path("barbie_flag", barbie_flag, name="barbie_flag"),
    path("notebook", notebook_view, name="notebook"),
    path("fallguy", fallguy_view, name="fallguy"),
    path("login", login_view, name="login"),
    path("piano", lala_view, name="piano"),
]
