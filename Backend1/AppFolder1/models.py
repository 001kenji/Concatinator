from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def _str_(self):
        return f"{self.name}{self.email}"
        