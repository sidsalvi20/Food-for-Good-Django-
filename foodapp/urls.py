from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views


urlpatterns = [
    path('',user_views.index,name="ShopHome"),
    path('about/',user_views.about,name="AboutUs"),
    path('contact/',user_views.contact,name="ContactUs"),
    path('tracker/',user_views.tracker,name="TrackingStatus"),
    path('cart/',user_views.cart,name="Cart"),
    path('productview/',user_views.prodView,name="products"),
    path('productview/indian',user_views.prodIndian,name="Indian cuisine"),
    path('productview/<name>/',user_views.detail,name="detail"),
    path('confirmation/',user_views.confirmView,name="confirmation"),
    path('register/',user_views.register,name="register"),
    path('add_comment/',user_views.add_comment,name="add_comment"),
    path('tracking/',user_views.track,name="track"),
    path('profile/',user_views.profile,name="profile"),
    path('update/',user_views.update_profile,name="update"),
    path('login/',auth_views.LoginView.as_view(template_name = 'foodapp/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'foodapp/login.html'),name="logout"), 
   
    

]

