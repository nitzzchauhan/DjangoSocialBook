from . import views  
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/',views.post_created, name='post_create'),
    path('<int:post_id>/edit/', views.post_edit, name = 'post_edit' ),
    path('<int:post_id>/delete/', views.post_delete, name = 'post_delete' ),
    path('register/', views.register, name = 'register' ),
    path('post/<int:post_id>/comment/add/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),
   
] 