from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from form.models import FORM
# Create your views here.
def submission(request):
    if request.method=='POST' :
    
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        FORM.objects.create(first_name=first_name,last_name=last_name,phone=phone,email=email,address=address)
    
        return redirect('/')
    
    Queryset=FORM.objects.all()
    return render(request,'form.html',context={'detail':Queryset})