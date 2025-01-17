from django.shortcuts import render,redirect
from .forms import GuranterForm
from .models import Guaranter


# Create your views here.
def GuaranterPOst(request):
    template_name='Guaranter/post.html'
    form = GuranterForm()
    if request.method == 'POST':
        form = GuranterForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,template_name,context)

def GuaranterGet(request):
    template_name = 'Guaranter/get.html'
    obj=Guaranter.objects.all()
    context={'obj':obj}
    return render(request,template_name,context)

def GuaranterPut(request,id):
    obj = Guaranter.objects.get(guaranterId=id)
    form = GuranterForm(instance=obj)
    if request.method == 'POST':
        form = GuranterForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('GUr_get_url')
    template_name='Guaranter/post.html'
    context = {'form':form}
    return render(request,template_name,context)

def GuaranterDelete(request,id):
    obj=Guaranter.objects.get(guaranterId=id)
    obj.delete()
    return redirect('GUr_get_url')