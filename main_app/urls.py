from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.create_widget, name='add_widget'),
    path('delete/<int:id>', views.delete, name='delete_widget')
]