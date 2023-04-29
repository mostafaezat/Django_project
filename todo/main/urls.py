from django.urls import  path
from . import views


urlpatterns = [
    path('', views.home , name="home"),  
    path('createtodo/', views.create_todo , name="createtodo"),
    path('createitem/<str:id>', views.create_item_todo , name="createitem"),
    path('updatetodo/<str:id>', views.updatetodo , name="updatetodo"),
    path('deletetodo/<str:id>', views.deletetodo , name="deletetodo"),
    path('detailed/<str:id>', views.detailed , name="detailed"),   
    path('completed/<str:id>' , views.completed , name="completed")
]