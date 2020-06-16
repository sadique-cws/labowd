from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView,View,DetailView

class HomeView(View):
    def get(self,request,*args,**kwargs):
        data = {
            "peoples":Peoples.objects.all(),
            "categories":Categories.objects.all()
        }
        return render(self.request,"home.html",data)


class PeopleDetailView(DetailView):
    model = Peoples
    template_name = "item.html"

    def get_context_data(self, **kwargs):
        context = super(PeopleDetailView, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        return context

class AddRecordView(View):
    form = AddRecordForm()

    def get(self,request,*args,**kwargs):
        data= {"form":self.form}
        return render(self.request,"addRecord.html",data)

    def post(self,request,*args,**kwargs):
        form = AddRecordForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            #todo : if not form is valid then what
            pass
