from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField(max_length=240)
#     photo = models.ImageField(upload_to='photos/',
#     blank = True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f'{self.user.username} - {self.text[:10]}'
    
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

#     def __str__(self):
#         return f'Comment by {self.user.username} on {self.post.id}'
















class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)  # Added likes field

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

    def total_likes(self):
        return self.likes.count()

# from myapp.models import Comment  # Replace 'myapp' with the actual app name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.id}'

    def total_likes(self):
        return self.likes.count()


    
