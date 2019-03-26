#from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='ndex'),
    path('cbt/',views.cbt.as_view(),name='ram'),
    path('cqt/',TemplateView.as_view(template_name='app1/index2.html')),
    path('register/',views.UserForm.as_view(),name='register'),

]
