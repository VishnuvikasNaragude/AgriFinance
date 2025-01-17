from django.shortcuts import render,redirect
from .forms import CibilForms
from .models import CibilScoreCheck



# Create your views here.


def CibilView(Request):
    template_name= 'cibilScore/post.html'
    form = CibilForms()
    if Request.method=='POST':
        form =CibilForms(Request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(Request,template_name,context)

def CibilGet(request):
    template_name='cibilScore/get.html'
    obj = CibilScoreCheck.objects.all()
    return render(request,template_name,context={'obj':obj})

def cibilPut(request,id):
       
       obj=CibilScoreCheck.objects.get(cibilId=id)
       form = CibilForms(instance=obj)
       if request.method=='POST':
            form = CibilForms(request.POST,instance=obj)
            if form.is_valid():
                 form.save()
            return redirect('cibil_get')
       template_name= 'cibilScore/post.html'
       context ={'form':form}
       return render(request,template_name,context)

def cibilDelete(request,id):
     obj = CibilScoreCheck.objects.get(cibilId=id)
     obj.delete()
     return redirect('cibil_get')

     
