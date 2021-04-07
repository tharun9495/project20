from django.urls import path
from app2 import views
app_name="app2"

urlpatterns=[
    path('index/',views.index,name="index"),
    path('sample/',views.sample,name="sample"),
    path("<city>/",views.carry_data,name="carry_data"),  

]