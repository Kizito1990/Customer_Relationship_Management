from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name ='logout'),
    path('register/', views.register_user, name ='register'),
    path('customer/<int:pk>', views.customer_records, name = 'customer'),
    path('delete<int:pk>/', views.delete, name = 'delete'),
    path('addrecord/', views.AddCustomer, name ='addrecord'),
    path('update/<int:pk>/', views.UpdateCustomer, name ='update'),
 
 ]
   