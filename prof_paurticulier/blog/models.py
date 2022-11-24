from django.db import models

from authentication.models import User

class Ticket(models.Model):
    class Types(models.TextChoices):
        INFORMATION = "Information"
        ERROR = "Erreur"
        BLOG = "Blog"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    content = models.TextField()
    type = models.CharField(choices=Types.choices, max_length=12, default="Blog")