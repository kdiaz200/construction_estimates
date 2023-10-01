from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('materials/', views.material_list, name='material_list'),
    path('favorite_materials/<int:id>/', views.favorite_material_detail, name='favorite_material_detail'),
    path('favorite_materials/', views.favorite_material, name='favorite_material'),
    path('get_user_favorites/', views.get_user_favorites, name='get_user_favorites'),
]

