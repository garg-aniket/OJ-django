from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question', views.test, name='question'),
    path('result', views.result, name='result'),
    path('submit', views.submitCode, name='submit'),
    path('runCode', views.runCode, name='runCode'),
    path('login', views.my_login, name='login'),
]