from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import ImageLikeToggle
from . import views 

urlpatterns=[
    url('^$',views.index,name='index.html'),
    url(r'^(?P<slug>[\w-]+)/like/$', ImageLikeToggle.as_view(), name='like-toggle'),
    url('^comment/(?P<id>\d+)',views.post_comment, name='comment'),
    url('^profile/$',views.profile, name='profile'),
    url(r'^edit/profile/$',views.edit_profile, name = 'edit-profile'),
    url('^upload/',views.upload, name='upload')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)