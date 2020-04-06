from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import historyManagement
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    #IP:- 127.0.0.1:8000/

    #Render Views
    path("", TemplateView.as_view(template_name="mainApp/login.html")),
    path("signup", TemplateView.as_view(template_name="mainApp/signup.html")),
    path("mainPage", views.mainPage, name="mainPage"),
    path("logout", LogoutView.as_view()),

    # Api's
    path('api/createUser/', views.createUser, name="createUser"),
    path('api/validateUser/', views.validateUser, name="validateUser"),
    path('historyManagement', historyManagement.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
