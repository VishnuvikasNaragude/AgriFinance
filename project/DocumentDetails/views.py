from django.shortcuts import render,redirect

# Create your views here.
from .forms import DocumentDetailsForm
from .models import DocumentDetails


# Create your views here.
def DocumentDetailsPOst(request):
    template_name='DocumentDetails/post.html'
    form = DocumentDetailsForm()
    if request.method == 'POST':
        form = DocumentDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,template_name,context)

def DocumentDetailsGet(request):
    template_name = 'DocumentDetails/get.html'
    obj=DocumentDetails.objects.all()
    context={'obj':obj}
    return render(request,template_name,context)

def DocumentDetailsPut(request,id):
    obj = DocumentDetails.objects.get(documentId=id)
    form = DocumentDetailsForm(instance=obj)
    if request.method == 'POST':
        form = DocumentDetailsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect('doc_get_url')
    template_name='DocumentDetails/post.html'
    context = {'form':form}
    return render(request,template_name,context)

def DocumentDetailsDelete(request,id):
    obj=DocumentDetails.objects.get(documentId=id)
    obj.delete()
    return redirect('doc_get_url')