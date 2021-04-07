from django.urls import path
from app3 import views
app_name="app3"

urlpatterns=[
    path('index/',views.index,name="index"),
    path('sample/',views.sample,name="sample"),   
    path("fact/<num>/",views.facto,name="facto"),

]