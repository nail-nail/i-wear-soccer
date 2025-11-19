from django.urls import path
from authentication.views import get_user_id, login, register, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('user-id/', get_user_id, name='user-id'),
]