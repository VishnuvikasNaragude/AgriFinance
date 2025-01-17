from django.shortcuts import render,redirect
from .forms import Vehicle,VehicleForm
# Create your views here.

def post(request):
    template_name='vehicle/post.html'
    form=VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render (request,template_name,context)
def get(request):
    obj=Vehicle.objects.all()
    template_name='vehicle/get.html'
    context={'obj':obj}
    return render(request,template_name,context)

def put(request,id):
    template_name='vehicle/post.html'
    obj=Vehicle.objects.get(vehicalId=id)
    form = VehicleForm(instance=obj)
    if request.method=='POST':
        form=VehicleForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,template_name,context)

def delete(request,id):
    
    obj=Vehicle.objects.get(vehicalId=id)
    obj.delete()    