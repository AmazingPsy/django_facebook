from django.db import models

# Create your models here.
class Article(models.Model):
    author      = models.CharField(max_length=120)
    title       = models.CharField(max_length=120)
    text        = models.TextField()
    password    = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article         = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    # 코멘트가 아티클에 종속된다.라고 설명한다. 글이 삭제되면 코멘트도 자동으로 삭제되라고 on_delete
    author          = models.CharField(max_length=120)
    text            = models.TextField()
    password        = models.CharField(max_length=120)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    # 모델 사양서를 만든것임