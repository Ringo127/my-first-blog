from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

# urlを作る
urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('article', views.article_list, name="article_list")
    #path('accounts/login/', LoginView.as_view(), name='login')
]