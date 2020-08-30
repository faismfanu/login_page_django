from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',views.login,name=""),
    path('admin/',views.admin, name="admin"),
    path('product',views.index,name="product"),
    path('login',views.login,name="login_url"),
    path('signh',views.register,name="signh"),
    path('logout',views.logout,name="logout"),
    path('add',views.add,name="add"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('update/<int:id>',views.update,name="update"),
    path('search',views.search,name='search'),
       
]