from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=200, null=False, blank=False)
    password = models.TextField(null=False, blank=False, editable=False)
    useremail = models.EmailField(null=False, blank=False)

    def __str__(self) -> str:
        return self.username