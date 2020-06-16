from django.shortcuts import render
from .models import *

from django.views.generic import ListView,View



# def Home(requst):
#     data = {"home":Peoples.objects.all()}
#     return render(requst,"home.html",data)



class HomeView(View):

    def get(self,request,*args,**kwargs):
        data = {
            "peoples":Peoples.objects.all(),
            "categories":Categories.objects.all()
        }
        return render(self.request,"home.html",data)



