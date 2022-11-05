from django.shortcuts import render
from .forms import ProductForm, Product
import requests
from .yolo.call2 import calling
import os
# Create your views here.
def home(request):
    return render(request, 'base.html')

def upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    image = Product.objects.all()   
    image1 = list(image)[0]
    image1  =  image1.image
    print(image1)
    #print(image1.image)
    calling()
    #responses = requests.get(f'http://shoeasy.me/shoEasy-api/?search={keyword}').json()


    image.delete()
    context = {
        'image' : image1,
    }
    return render(request, 'base.html')

