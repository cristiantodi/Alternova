from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
