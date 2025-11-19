import datetime
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from django.utils.html import strip_tags
from main.models import Shop
from main.forms import ProductForm
import json
import requests
from decimal import Decimal, InvalidOperation



def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = strip_tags(data.get("title", ""))  # Strip HTML tags
        content = strip_tags(data.get("content", ""))  # Strip HTML tags
        name = strip_tags(data.get("name", ""))
        price = strip_tags(data.get("price", ""))
        description = strip_tags(data.get("title", ""))
        rating = strip_tags(data.get("rating", ""))
        stock = strip_tags(data.get("stock", ""))
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Shop(
        user=user,
        name = name,
        price = price,
        description = description,
        thumbnail = thumbnail,
        category = category,
        is_featured = is_featured,
        rating = rating,
        stock = stock
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Shop.objects.all()
    else:
        product_list = Shop.objects.filter(user=request.user)
    context = {
        'app': 'I WEAR SOCCER',
        'name': 'Naila Khadijah',
        'class' : 'PBP C',
        'product_list': product_list,
        'last_login' : request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)
# Create your views here.

@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if request.method == "POST":
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()

            if is_ajax:
                return JsonResponse({
                    "success": True,
                    "message": "Product created successfully.",
                    "product": serialize_product(product_entry),
                })
            return redirect("main:show_main")

        if is_ajax:
            return JsonResponse(
                {"success": False, "errors": form.errors},
                status=400,
            )

    return render(request, "add_product.html", {"form": form})


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Shop, pk=id)

    context = {
        'product': product
    }
    return render(request, "product_detail.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

        if form.is_valid():
            form.save()
            if is_ajax:
                return JsonResponse({"success": True, "redirect_url": reverse("main:login")})
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")

        if is_ajax:
            return JsonResponse(
                {"success": False,
                "errors": form.errors,
                "non_field_errors": form.non_field_errors()},
                status=400,
            )

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if is_ajax:
                response = JsonResponse({"success": True, "redirect_url": reverse("main:show_main")})
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

        if is_ajax:
            return JsonResponse(
                {"success": False,
                "errors": form.errors,
                "non_field_errors": form.non_field_errors()},
                status=400,
            )
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"
    logout(request)
    redirect_url = reverse('main:login')
    if is_ajax:
        response = JsonResponse({"success": True, "redirect_url": redirect_url})
    else:
        response = HttpResponseRedirect(redirect_url)
    response.delete_cookie('last_login')
    return response



@login_required(login_url='/login')
@require_POST
@csrf_exempt
def add_product_entry_ajax(request):
    form = ProductForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({"success": False, "errors": form.errors}, status=400)

    product = form.save(commit=False)
    product.user = request.user
    product.save()

    return JsonResponse(
        {
            "success": True,
            "message": "Product created successfully.",
            "product": serialize_product(product),
        },
        status=201,
    )


def show_xml(request):
     product_list = Shop.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Shop.objects.all()
    data = [serialize_product(product) for product in product_list]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
   try:
       product_item = Shop.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
   try:
        product = Shop.objects.get(pk=product_id)
        data = serialize_product(product)
        return JsonResponse(data)
   except Shop.DoesNotExist:
       return JsonResponse({'detail': 'Not found'}, status=404)
   
@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Shop, pk=id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if request.method == "POST":
        if form.is_valid():
            updated_product = form.save()

            if is_ajax:
                return JsonResponse({
                    "success": True,
                    "message": "Product updated successfully.",
                    "product": serialize_product(updated_product),
                })
            return redirect("main:show_main")

        if is_ajax:
            return JsonResponse(
                {"success": False, "errors": form.errors},
                status=400,
            )

    return render(request, "edit_product.html", {"form": form, "product": product})


@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Shop, pk=id, user=request.user)
    is_ajax = request.headers.get("X-Requested-With") == "XMLHttpRequest"

    if request.method == "POST":
        product.delete()
        if is_ajax:
            return JsonResponse({"success": True, "deleted_id": id})
        return HttpResponseRedirect(reverse('main:show_main'))

    if is_ajax:
        return JsonResponse({"success": False, "message": "Unsupported method."}, status=405)

    return HttpResponseRedirect(reverse('main:show_main'))

def serialize_product(product):
    return {
        "id": str(product.id),
        "name": product.name,
        "price": product.price,
        "description": product.description,
        "category": product.category,
        "thumbnail": product.thumbnail,
        "purchase_count": product.purchase_count,
        "is_featured": product.is_featured,
        "rating": float(product.rating) if getattr(product, "rating", None) is not None else None,
        "stock": product.stock,
        "created_at": product.created_at.isoformat() if getattr(product, 'created_at', None) else None,
        "user_id": product.user_id,
    }

