from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import BankDetailsForm
from .models import BankDetails


# Create your views here.
def BankDetailspostView(Request):
    template_name= 'BankDetails/post.html'
    form = BankDetailsForm()
    if Request.method=='POST':
        form =BankDetailsForm(Request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(Request,template_name,context)

def BankDetailsget(request):
    template_name='BankDetails/get.html'
    obj = BankDetails.objects.all()
    context = {'boj':obj}
    return render(request,template_name,context)

def BankDetailsUpdate(request,id):
    
    obj = BankDetails.objects.get(bankId=id)
    form = BankDetailsForm(instance=obj)
    if request.method=='POST':
        form = BankDetailsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()

        return redirect('bank_get_url')
    template_name= 'BankDetails/post.html'
    context = {"form": form}
    return render(request,template_name,context)

def BankDetailsDelete(request,id):
    
   obj =BankDetails.objects.get(bankId=id)
   obj.delete()
   return redirect('bank_get_url')


