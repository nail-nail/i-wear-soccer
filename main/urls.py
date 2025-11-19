from django.urls import path
from main.views import add_product_entry_ajax, create_product_flutter, delete_product, edit_product, proxy_image, show_main, show_xml,  show_json,  show_xml_by_id, show_json_by_id, add_product, show_product, logout_user, login_user, register

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('add-product/', add_product, name='add_product'),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('product/create-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
