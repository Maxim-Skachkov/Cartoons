from django.db import models


class CommonFields(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.SlugField(unique=True)

    def __str__(self) -> str:
        return str(self.name)


