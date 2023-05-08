from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category
from tipo.models import Tipo


class Post(models.Model):
    title = models.CharField(max_length=255)
    miniature = models.ImageField(upload_to='static/admin/img/', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=SET_NULL, null=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.title
