from django.shortcuts import render,redirect
from .models import Enquiry
from .forms import EnquriForms

# Create your views here.


def EnqueryView(Request):
    template_name ="EnqueryView.html"
    form = EnquriForms()
    if Request.method =="POST":
        form =EnquriForms(Request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(Request,template_name,context)


def EnqueryShow(request):
    template_name ="EnqueryShow.html"
    obj = Enquiry.objects.all()
    context = {"data":obj}
    return render(request,template_name,context)

def EnqueryUpdate(request,id):
    obj = Enquiry.objects.get(enq_id=id)
    form = EnquriForms(instance=obj)
    
    if request.method == "POST":
        form = EnquriForms(request.POST, instance=obj)
        if form.is_valid():  
            form.save()  
            return redirect('get_url')  

    template_name = "EnqueryView.html"
    context = {"form": form}

    return render(request, template_name, context)

def EnqueryDelete(request,id):
    template_name = "EnqDelete.html"
    
    if request.method=='POST':   
        obj = Enquiry.objects.get(enq_id=id)
        obj.delete()
        return redirect('get_url')
    return render(request, template_name, context={})
