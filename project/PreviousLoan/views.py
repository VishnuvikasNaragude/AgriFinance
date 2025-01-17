from django.shortcuts import render,redirect
from .forms import PreviousLoanForm
from .models import PreviousLoan
# Create your views here.


def PreviousLoanPOst(request):
    template_name='PreviousLoan/post.html'
    form = PreviousLoanForm()
    if request.method == 'POST':
        form = PreviousLoanForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,template_name,context)

def PreviousLoanGet(request):
    template_name = 'PreviousLoan/get.html'
    obj=PreviousLoan.objects.all()
    context={'obj':obj}
    return render(request,template_name,context)

def PreviousLoanPut(request,id):
    obj = PreviousLoan.objects.get(previousloanId=id)
    form = PreviousLoanForm(instance=obj)
    if request.method == 'POST':
        form = PreviousLoanForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('pre_get_url')
    template_name='PreviousLoan/post.html'
    context = {'form':form}
    return render(request,template_name,context)

def PreviousLoanDelete(request,id):
    obj=PreviousLoan.objects.get(previousloanId=id)
    obj.delete()
    return redirect('pre_get_url')