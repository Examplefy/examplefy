from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from haystack.generic_views import SearchView

from django.views.generic import TemplateView
import examplefy.views
from examplefy.views import *

# Basics
urlpatterns = patterns('',
    # homepage
    url(r'^$', examplefy.views.homepage, name="homepage"),

    url(r'^search/', ExampleSearchView.as_view(), name='haystack_search'),
    #url(r'^search/', include('haystack.urls')),

    # admin site
    url(r'^admin/', include(admin.site.urls)),

    # viewing an example
    url(r'^example/$', ExampleView.as_view(), name='example'),

    # Asking a question
    url(r'^ask/$', ask_view, name='ask'),

    # Adding an example
    url(r'^add_example', add_example_view, name='add_example'),

    # Getting examples by ajax
    # url(r'^get_examples', get_examples, name='get_examples'),
    url(r'^get_examples_json', get_examples_json, name='get_examples_json'),
    # url(r'^get_example_by_id', get_example_by_id, name='get_example_by_id'),
)



# Authentication
urlpatterns += patterns('',
    url(r'^login/$', login, { 'redirect_field_name': '/' }, name='login'),

    url(r'^logout/$', logout, { 'template_name': 'index.html', 'next_page': '/' }, name='logout'),

    url(r'^password_reset/$', password_reset, {
    'template_name': 'registration/password_reset.html',
    'email_template_name': 'registration/password_reset_email.html',
    'subject_template_name': 'registration/password_reset_subject.txt',
    'post_reset_redirect': '/password_reset_done',
    'from_email': 'calpeyser@gmail.com', # TODO: replace with a domain email
    }, name='password_reset'),

    url(r'^password_reset_done/$', password_reset_done, {
    'template_name': 'registration/password_reset_done_custom.html',
    }, name='password_reset_done'),

    url(r'^password_reset_confirm$', password_reset_confirm, name="password_reset_confirm"),

    url(r'^password_reset_complete$', password_reset_complete, name="password_reset_complete"),
)
