from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "products"

urlpatterns = [

    path('',views.Productview.as_view(), name='index'),
    path('product/',views.Product.as_view(), name='product'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('subcategory/', views.Subcategory.as_view(), name='subcategory'),


    


    
    
]