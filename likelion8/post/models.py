from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 작성시간
    updated_at = models.DateTimeField(auto_now=True) # 수정시간

    def __str__(self):
        return self.title

    # DB에서는 길이제한 유무에 따라서 문자열 필드타입이 달라집니다.
    # 길이 제한이 없는 문자열을 많이 쓰면 성능이 좋지 않다.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


