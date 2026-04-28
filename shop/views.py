from django.shortcuts import render,redirect
from .forms import MyUserForm
from django.contrib.auth import login,logout,authenticate
from .models import Clothes
from django.db.models import Q#QuerySet

def registration(request):
    
    if request.method=='POST':
        forms = MyUserForm(request.POST)
        if forms.is_valid():
            user=  forms.save()
            login(request,user)
            return redirect('home')
        
    else:
        forms=MyUserForm()
    return render(request,'regis.html',{'forms':forms})


def homepage(request):
    clothes = Clothes.objects.all()
    query = request.GET.get('q')

    if query:
        clothes = clothes.filter(
            Q(title__icontains=query) |
            Q(brand__brand_name__icontains=query) |
            Q(color__color_name__icontains=query)
        ).distinct()

    con = {'clothes': clothes,
           'query': query}

    return render(request, 'home.html', con)

def shigiw(request):
    logout(request)
    return redirect('home')