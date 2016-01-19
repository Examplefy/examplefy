from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from carts.views import CartView
import questions.views
from questions.views import IndexView, DetailView, ResultsView, CreateQuestionView, EditQuestionView

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
    url(r'^about/$', 'ecommerce.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^products/', include('products.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^categories/', include('products.urls_categories')),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    # url(r'^questions/$', questions.views.IndexView.as_view(), name='index'),
    # url(r'^questions/(?P<pk>[0-9]+)/$', questions.views.DetailView.as_view(), name='detail'),
    # url(r'^questions/(?P<pk>[0-9]+)/results/$', questions.views.ResultsView.as_view(), name='results'),
    # url(r'^questions/(?P<question_id>[0-9]+)/vote/$', questions.views.vote, name='vote'),
    # url(r'^questions/create/$', questions.views.CreateQuestionView.as_view(), name='create'),
    # url(r'^questions/edit/(?P<pk>\d+)/$', questions.views.EditQuestionView.as_view(), name='edit'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)