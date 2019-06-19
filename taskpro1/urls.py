"""taskpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from taskapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.emp_reg),
    url(r'^emp$', views.emp_data, name='emp'),
    url(r'^edit/(?P<id>\d+)', views.edit, name='edit'),
    url(r'^update/(?P<id>\d+)', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)', views.delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns +=[
#         url(r'^media/(?P<path>.*)$',serve,{
#             'document_root':settings.MEDIA_ROOT,
#         }),
#     ]
