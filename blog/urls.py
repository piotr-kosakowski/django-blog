from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
 path('', views.index, name='index'),
 path('posts/<int:post_id>', views.post, name='post'),
 path('register/', views.register_view, name='register'),
 path('logout/', views.logout_view, name='logout'),
 path('new_post/', views.new_post, name='new_post'),
 path('new_topic/', views.new_topic, name='new_topic'),
 path('topics/<int:topic_id>', views.topic, name='topic'),
 path('like_post/<int:post_id>/', views.like_post, name='like_post'),
 path('check_like_post/<int:post_id>/', views.check_like_post, name='check_like_post'),
 path('all_posts/', views.all_posts, name='all_posts'),
 path('all_topics/', views.all_topics, name='all_topics'),
 path('login/', CustomLoginView.as_view(), name='login'),

]
