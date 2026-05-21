from django.db import models


class Profile(models.Model):
    full_name   = models.CharField(max_length=200)
    nickname    = models.CharField(max_length=100)
    birth_place = models.CharField(max_length=100)
    birth_date  = models.DateField()
    description = models.TextField()
    photo       = models.ImageField(upload_to='profile/', blank=True, null=True)
    instagram   = models.URLField(blank=True)
    linkedin    = models.URLField(blank=True)
    email       = models.EmailField(blank=True)

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    title       = models.CharField(max_length=200)
    company     = models.CharField(max_length=200)
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True)
    is_current  = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} — {self.company}"