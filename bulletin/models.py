from django.db import models
from authorization.models import Account

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def comments(self):
        return self.comment_set.all()
    
    @property
    def likes(self):
        return self.like_set.all()

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to {self.post.title}"
    
class Like(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} liked {self.post}"
