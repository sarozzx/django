from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('kathmandu',views.index1,name='index1'),
    path('pokhara',views.index2,name='index2')
]