from django.urls import path
from .views import CategoryListView, ProductDetailView, ProductCreateView,ProductEdit,ProductDelete,ProductSavat


urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/delete', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/edit', ProductEdit.as_view(), name='product_edit'),
    path('savat/', ProductSavat, name = 'savat'),
]