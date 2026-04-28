from django.urls import path
from .views import registration,homepage,shigiw
urlpatterns = [
    path('', homepage, name='home'),
    path('search/', homepage, name='search'),
    path('logout/', shigiw, name='logout'),
    path('registraciya/', registration, name='reg'),
]