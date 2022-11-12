from django.shortcuts import render
from .forms import ProductForm, Product
import requests
from .yolo.call2 import calling
from .comment_classifier import get_responses
import os
from textblob import TextBlob
import re
import pandas as pd
import pandas as pd
import numpy as np
from textblob import TextBlob
import re
import urllib.request
from PIL import Image
import glob
import urllib
from .similarity_2 import check_similar


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
    with open('/home/sandeep/Desktop/major/CBIR/test.txt', 'r+') as f:
        keyword=f.readline()
        f.truncate(0)
    print(keyword)
    #keyword="Goldstar Black Sports"
    responses = requests.get(f'http://shoeasy.me/shoEasy-api/?search={keyword}').json()
    print(responses)
    df_product=list(get_responses(responses))
    img_lst=[]
    for item in df_product:
        img_lst.append(item+".jpg")
    print(img_lst)


    # removing files in directory
    removing_files = glob.glob('/home/sandeep/Desktop/major/CBIR/Json_response_images/*')
    for i in removing_files:
        os.remove(i)

    # downloading images in directory

    for response in responses:
        print(response)
        name = response['product_name']
        print(name)
        url = response['images']
        print(url)
        testImage = urllib.request
        testImage.urlretrieve(url, f'/home/sandeep/Desktop/major/CBIR/Json_response_images/{name}.jpg')

    img_lst=check_similar(img_lst)
    print(img_lst)