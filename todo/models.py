from django.db import models

class Todo(models.Model):
    # title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성시
    updated_at = models.DateTimeField(auto_now=True) # 수정시
    is_done = models.BooleanField(default=False) # 완료시
    
    def __str__(self) -> str:
        return self.content # 적은 내용 그대로 제목처럼 보여줌
    

