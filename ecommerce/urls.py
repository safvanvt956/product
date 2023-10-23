from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("product.urls", namespace="product")),
    path("", include("web.urls", namespace="web")),
    path("order", include("order.urls", namespace="order")),
    path("main", include("main.urls", namespace="main")),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
