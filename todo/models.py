from django.db import models

class Todo(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE) #유저 아이디가 삭제된다면 cascade는 글 전부 삭제
    # title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 생성시
    updated_at = models.DateTimeField(auto_now=True) # 수정시
    is_done = models.BooleanField(default=False) # 완료시
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.content # 적은 내용 그대로 제목처럼 보여줌
    

