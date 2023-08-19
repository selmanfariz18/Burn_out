from django.urls import path
from . import views
from Burn_out import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signin', views.signin, name="signin"),
    path('register',views.register, name="register"),
    path('logout',views.logout_user,name='logout_user'),
    path('user_page/', views.user_page, name='user_page'),  #basic userpage
    path('start_pomodoro/', views.start_pomodoro, name='start_pomodoro'),
    path('stop_pomodoro/', views.stop_pomodoro, name='stop_pomodoro'),
]