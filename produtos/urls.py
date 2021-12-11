from django.urls import path

from produtos.views import (
    index, 
    ola, 
    CreateCategoryView,
    ListCategoryView,
    CreateProductView,
    DetailCategoryView,
    UpdateCategoryView,
    DeleteCategoryView,
)

urlpatterns = [
    path('index/', index, name="index"),
    path('ola/', ola, name="ola"),
    path('category/add',
        CreateCategoryView.as_view(),
        name='create_category'),
    path('category',
        ListCategoryView.as_view(),
        name = 'list_category'),
    path('product/',
        CreateProductView.as_view(),
        name = 'create_product'),
    path('category/<int:pk>', 
        DetailCategoryView.as_view(),
        name='category_detail'),
    path('category/<int:pk>/update',
        UpdateCategoryView.as_view(),
        name='category_update'),
    path('category/<int:pk>/delete',
        DeleteCategoryView.as_view(),
        name='category_delete'),
]