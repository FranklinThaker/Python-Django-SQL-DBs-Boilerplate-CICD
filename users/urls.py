from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllUsers, name='list'),
    path('addUser/', views.addUser, name='add'),
    path('deleteUser/<id>', views.deleteUser, name='delete'),
    path('updateUser/<id>', views.updateUser, name='update'),
]
