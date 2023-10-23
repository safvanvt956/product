from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "order"

urlpatterns = [
    
    path("", views.order.as_view(),name='order'),

    
]