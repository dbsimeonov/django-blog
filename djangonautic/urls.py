from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    path('about/', views.about),
    path('', views.homepage)
]