from django.urls import path
from . import views
from Burn_out import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="home"),
    path('home',views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('register',views.register, name="register"),
    path('logout',views.logout_user,name='logout_user'),
    path('user_page/', views.user_page, name='user_page'),  #basic userpage
    path('start_pomodoro/', views.start_pomodoro, name='start_pomodoro'),
    path('stop_pomodoro/', views.stop_pomodoro, name='stop_pomodoro'),
    path('todo_list',views.todo_list, name='todo_list'),
    path('spotify-auth/', views.spotify_auth, name='spotify-auth'),
    path('callback/', views.spotify_callback, name='spotify-callback'),
    path('play/', views.play_track, name='play-track'),
    path('pause/', views.pause_track, name='pause-track'),
]