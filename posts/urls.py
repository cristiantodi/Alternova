from django.urls import path
from posts import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Home"),
    path('category/<int:category_id>/', views.category, name="Category"),
    path('tipo/<int:tipo_id>/', views.tipo, name="Tipo"),
    
]