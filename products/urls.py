from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import ProductDetailView, ProductListView, ExampleView, VariationListView

urlpatterns = [
    # Examples:
    #url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^(?P<pk>\d+)/inventory/$', VariationListView.as_view(), name='product_inventory'),
    url(r'^create/$', 'products.views.create_view', name='create_view'),    
    url(r'^(?P<pk>\d+)/edit/$', 'products.views.update_view', name='update_view'), 
    # viewing an example
    url(r'^example/$', ExampleView.as_view(), name='example'),
    #url(r'^(?P<id>\d+)', 'product.views.product_detail', name='product_detail_view_func'),
]