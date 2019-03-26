from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView,View
from .forms import UserForm
# Create your views here.
#functionbasedviews
def index(request):
   template= loader.get_template('app1/index1.html')
   context={
   }
   return HttpResponse(template.render(context,request))

#def index1(request):
#    return HttpResponse("this is a page")

#classbasedviews
class cbt(TemplateView):
    template_name='app1/index1.html'

class UserForm(View):
    form_class=UserForm
    template_name='app1/register.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            phone_number=form.cleaned_data['phone_number']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('weather:index')

        return render(request,self.template_name,{'form':form})