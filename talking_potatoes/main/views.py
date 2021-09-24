from django.shortcuts import render, redirect
from django.utils import timezone
# Create your views here.
from .models import Likelion
from .models import Growl

# Create your views here.

# 멋사 read 페이지 
def likelion_read(request) : 
    likelion = Likelion.objects.all()
    growl = Growl.objects.all()
    context ={
        'likelion' : likelion,
        'growl' : growl,
    }
    return render(request, 'likelion.html', context)

# 멋사 Create
def likelion_create(request) :
    if (request.method == 'POST'):
        post = Likelion()
        post.likelion_first = request.POST['likelion_first']
        post.likelion_second = request.POST['likelion_second']
        post.created = timezone.datetime.now()
        post.writer = request.user
        post.save()
        return redirect('likelion_read')

# 어흥 Create
def growl_create(request) :
    if (request.method == 'POST'):
        obj = Growl()
        obj.growl_first = request.POST['growl_first']
        obj.growl_second = request.POST['growl_second']
        obj.created = timezone.datetime.now()
        obj.writer = request.user
        obj.save()
        return redirect('likelion_read')


