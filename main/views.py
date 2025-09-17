from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers
from main.models import Shop
from main.forms import ProductForm

def show_main(request):
    product_list = Shop.objects.all()
    context = {
        'app': 'I WEAR SOCCER',
        'name': 'Naila Khadijah',
        'class' : 'PBP C',
        'product_list': product_list
    }

    return render(request, "main.html", context)
# Create your views here.

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Shop, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)
def show_xml(request):
     product_list = Shop.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Shop.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
   try:
       product_item = Shop.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
       product_item = Shop.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)