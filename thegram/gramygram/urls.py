from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import ImageLikeToggle
from . import views 

urlpatterns=[
    url('^$',views.index,name='index.html'),
    url(r'^(?P<slug>[\w-]+)/like/$', ImageLikeToggle.as_view(), name='like-toggle'),
    url(r'^new/comment$', views.new_comment, name='new-comment')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)