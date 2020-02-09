from django.conf.urls import include, url
from django.contrib import admin
from example import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
