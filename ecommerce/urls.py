from django.contrib import admin
from django.urls import path
from shopping.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('about/',About,name="about"),
    path('contact/',contact,name="contact"),
    path('blog/',blog,name="blog"),
    path('cart/',cart,name="cart"),
    path('cat_details/<int:cid>/',shop,name="shop"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
