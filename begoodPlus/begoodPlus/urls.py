"""begoodPlus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from pages.views import order_form, order_form2, order_form3,catalog_view,catalog_page, landing_page_view, my_logo_wrapper_view, catalog_page2
                        
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from rest_framework import routers
from product.views import ProductViewSet
from category.views import CategoryViewSet
from productImages.views import ProductImageViewSet
from catalogImages.views import CatalogImageViewSet
from product.views import products_select_all, products_select, product_detail
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'productImages', ProductImageViewSet)
router.register(r'CatalogImages', CatalogImageViewSet)
from provider.views import api_providers
from packingType.views import api_packing_types
from productSize.views import api_product_sizes
from productColor.views import api_product_colors
from stock.views import add_multiple_stocks
from clientLikedImages.views import add_liked_images
urlpatterns = [
    #path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('', landing_page_view),
    path('order/', order_form),
    path('order2/', order_form2),
    path('order3/', order_form3),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('order/products_select/<str:phrash>', products_select),
    path('order/products_select/', products_select_all), # TODO: delete in prod 
    path('products_select/', products_select_all),
    path('product_detail/<int:id>', product_detail),
    #re_path(r'catalog/(?P<slug>[\w\d\-\_]+)/$', catalog_page, name='albumView'),
    re_path(r'catalog/(?P<hierarchy>.+)/$', catalog_page, name='albumView'),
    re_path(r'catalog2/(?P<hierarchy>.+)/$', catalog_page2, name='albumView2'),
    path('begood-plus', catalog_view),
    path('my-logo', my_logo_wrapper_view),
    path('api/providers', api_providers), 
    path('api/packingTypes', api_packing_types),
    path('api/productSizes', api_product_sizes),
    path('api/productColors', api_product_colors),
    path('api/add_multiple_stocks', add_multiple_stocks),
    path('add_liked_images', add_liked_images),
]

if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
