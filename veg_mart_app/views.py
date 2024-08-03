from django.shortcuts import render
from .models import Vegetable

def home(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'home.html', {'vegetables': vegetables})


def product_detail(request, pk):
    vegetable = Vegetable.objects.get(id=pk)
    return render(request, 'product_details.html', {'vegetable': vegetable})
