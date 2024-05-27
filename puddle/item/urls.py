from django.urls import path

from . import views
app_name = 'item'

urlpatterns = [
    path('new/', views.new, name='new'),
     path('', views.browse, name='browse'),
    
    path('<int:pk>/', views.details, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    
]