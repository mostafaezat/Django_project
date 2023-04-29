from django.urls import include, path
from . import views


urlpatterns = [
    path('base/', views.base , name="base"),
    path('register/', views.registration , name="register"),
    path('login/', views.user_login , name="login"),
    path('logout/', views.user_logout , name="logout"),
]