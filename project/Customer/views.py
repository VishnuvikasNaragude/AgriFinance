from django.shortcuts import render,redirect
from .forms import CustomerForms
from .models import Customer


# Create your views here.
def CustomerView(Request):
    template_name= 'Customer/customer.html'
    form = CustomerForms()
    if Request.method=='POST':
        form =CustomerForms(Request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(Request,template_name,context)

def CustomerDetails(request):
    template_name='Customer/CusDetails.html'
    obj = Customer.objects.all()
    context = {'boj':obj}
    return render(request,template_name,context)

def CustomerUpdate(request,id):
    
    obj = Customer.objects.get(customerId=id)
    form = CustomerForms(instance=obj)
    if request.method=='POST':
        form = CustomerForms(request.POST,instance=obj)
        if form.is_valid():
            form.save()

        return redirect('C_get_url')
    template_name= 'Customer/customer.html'
    context = {"form": form}
    return render(request,template_name,context)

def CustomerDelete(request,id):
    
   obj =Customer.objects.get(customerId=id)
   obj.delete()
   return redirect('C_get_url')


