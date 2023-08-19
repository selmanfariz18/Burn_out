from django.urls import path
from . import views
from Burn_out import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('register',views.register, name="register"),
    path('home',views.home, name='home'),
    path('logout',views.logout_user,name='logout_user'),
]