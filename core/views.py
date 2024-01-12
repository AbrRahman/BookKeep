from django.shortcuts import render,redirect
from books.models import Book,Category
def landingPage(request):
    return redirect("home")
def home(request,cat_id=None):
    data=Book.objects.all()

    categories=Category.objects.all()
    if cat_id is not None and cat_id != 'all':
        category=Category.objects.get(slug=cat_id)
        data=Book.objects.filter(categories=category)
    return render(request,'index.html',{'books':data,'categories':categories})