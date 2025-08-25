from django.urls import path
from django.conf import settings
from django.utils.module_loading import import_string
from .views import (
    HomePageView, AboutPageView, ContactPageView,
    ProductIndexView, ProductShowView, ProductCreateView,
    CartView, CartRemoveAllView, ImageViewFactory, ImageViewNoDI
)

# Cargar la clase de storage definida en settings.py
ImageStorageClass = import_string(settings.IMAGE_STORAGE_CLASS)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'), 

    # ahora usamos la clase importada dinámicamente
    path('image/', ImageViewFactory(ImageStorageClass()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageStorageClass()).as_view(), name='image_save'),

    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('image/save', ImageViewNoDI.as_view(), name='imagenodi_save'),
]
