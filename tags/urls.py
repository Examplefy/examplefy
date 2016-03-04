from django.conf.urls import include, url
from django.contrib import admin

from .views import TagListView, TagDetailView

urlpatterns = [
    # Examples:
    #url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^$', TagListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', TagDetailView.as_view(), name='tag_detail'), 
    #url(r'^(?P<id>\d+)', 'product.views.product_detail', name='product_detail_view_func'),
]