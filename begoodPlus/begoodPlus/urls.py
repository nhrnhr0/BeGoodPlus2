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
from catalogAlbum.views import CatalogAlbumViewSet
from product.views import products_select_all, products_select, product_detail
from freeFlow.views import FfStoreViewSet
from color.views import ColorsViewSet
from productSize.views import SizesViewSet
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'productImages', ProductImageViewSet)
router.register(r'CatalogAlbums', CatalogAlbumViewSet)
router.register(r'CatalogImages', CatalogImageViewSet)

router.register(r'freeFlowStores', FfStoreViewSet)
router.register(r'colors', ColorsViewSet)
router.register(r'sizes', SizesViewSet)
from provider.views import api_providers
from packingType.views import api_packing_types
from productSize.views import api_product_sizes
from productColor.views import api_product_colors
from stock.views import add_multiple_stocks
from clientLikedImages.views import add_liked_images
from clientImages.views import upload_user_image
from glofa_types.views import glofa_data
from freeFlow.views import freeFlowView, freeFlowChangeLanguage
from core.views import admin_subscribe_view, mainView, saveBaseContactFormView,autocompleteModel, autocompleteClick
from leadsCampains.views import landingPageFormSubmit
from catalogAlbum.views import catalogView2,catalogView_api
from myUserTasks.views import updateContactFormUserTaskView, getUserTasksView,updateProductsFormUserTaskView,getUserCartView,delUserLikedProductView
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
    path('upload_user_image', upload_user_image),
    path('glofa_data/<int:id>', glofa_data),
    path('freeFlow/', freeFlowView),
    path('freeFlow/<str:lang>/', freeFlowView),
    path('adminSub', admin_subscribe_view),
    re_path('^webpush/', include('webpush.urls')),
    #path('TaxReturnCampain/', TaxReturnCampainView)
    path('landingPageFormSubmit', landingPageFormSubmit),
    path('saveContactForm/<path:next>/', saveBaseContactFormView, name="save-contact-form"),

    path('test/', mainView, name='main-view'),
    path('testCatalog', catalogView2,name="catalogView2"),
    path('catalog_api', catalogView_api, name="catalog-view-api"),
    path('tasks/update-contact-form', updateContactFormUserTaskView, name='update-contact-form-user-task'),
    #path('tasks/submit-contact-form', submitContactFormUserTaskView, name='submit-contact-form-user-task'),
    path('tasks/update-products-form', updateProductsFormUserTaskView, name='update-products-form-user-task'),
    path('tasks/get-user-tasks', getUserTasksView, name='get-user-tasks'),
    path('tasks/get-user-cart', getUserCartView, name='get-user-cart'),
    path('tasks/delete-user-liked-product/', delUserLikedProductView, name='delete-user-liked-product'),
    path('search',autocompleteModel),
    path('search-click', autocompleteClick),
]

if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
