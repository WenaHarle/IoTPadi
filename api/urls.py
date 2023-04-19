from django.urls import path
from . import views


urlpatterns = [
    path('data-list/', views.ShowAll, name='data-list'),
    path('data-detail/<int:pk>/', views.ViewData, name='data-detail'),
    path('data-create/', views.CreateData, name='data-create'),
    path('data-update/<int:pk>/', views.updateData, name='data-update'),
    path('data-delete/<int:pk>/', views.deleteData, name='data-delete'),
    path('data/add/', views.create_data, name='create_data'),
]
