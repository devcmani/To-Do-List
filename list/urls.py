from unicodedata import name
from django.contrib import admin
from django.urls import path
from list import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show/',views.show_data,name="show"),
    path("update/<int:id>/",views.update,name="update"),
    path("updating/<int:id>/",views.updating,name="updating"),
    path("delete/<int:id>/",views.delete,name="delete")

]