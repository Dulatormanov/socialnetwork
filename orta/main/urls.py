from django.urls import path, include
from. import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    path('',views.index,name='index'),
    path('register/',views.registerForm,name='register'),
    path('home',views.home,name='home'),
    path('logout/',auth_views.LogoutView.as_view(template_name='main/logout.html'),name='logout'),
    path('news/',views.news,name='news'),
    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),
    path('comment/<username>/<post_id>/', views.comment,name = 'comment'),
    path('profile/<username>/', views.profile,name='profile'),
    path('postweb/<username>/', views.postweb,name='postweb'),
    path('welcome/',views.welcome,name='welcome'),
    path('search/', views.search, name='search'),

]
