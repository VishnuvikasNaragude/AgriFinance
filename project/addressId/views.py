from django.shortcuts import render,redirect
from .forms import AddressForm
from .models import Address


# Create your views here.
def AddresPOST(request):
    template_name = 'addressId/post.html'
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,template_name,context)

def AddresGet(request):
    template_name = 'addressId/get.html'
    obj = Address.objects.all()
    context = {'obj':obj}
    return render(request,template_name,context)

def AddresPut(request,id):
    
    obj = Address.objects.get(addressId=id)
    form = AddressForm(instance=obj)
    if request.method == 'POST':
        form = AddressForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('ADD_get')
    template_name = 'addressId/post.html'
    context = {'form':form}
    return render(request,template_name,context)

def AddresDelete(request,id):
    obj = Address.objects.get(addressId=id)
    obj.delete()
    return redirect('ADD_get')