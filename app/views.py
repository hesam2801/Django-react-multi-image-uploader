from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import random
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


# Create your views here.


def index(request):
    product_objects = Product.objects.all()
    image_objects = Image.objects.all()
    products = [{"name": product_object.name, "description": product_object.description,
                 "images": [f"http://{request.get_host()}{image_object.link}" for image_object in image_objects if product_object == image_object.product]
                 } for product_object in product_objects]
    print(products)
    return JsonResponse({'error': 0, 'message': 'succeed', 'products': products})

def save(request):
    name=request.POST["name"]
    description=request.POST["description"]
    f_names = request.FILES.getlist("images")
    product = Product.objects.create(name = name, description = description)
    fs = FileSystemStorage()
    for f_name in f_names:
        rnd = random.randint(1, 1000000)
        img_format = str(f_name).split('.')[-1]
        fn = fs.save(str(rnd) + f".{img_format}", f_name)
        uploaded_file_url = fs.url(fn)
        Image.objects.create(
            link = uploaded_file_url,
            product = product
        )
    return JsonResponse({'error': 0, 'message': 'succeed'})
