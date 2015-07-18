from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to='media')
    large_thumbnail = models.ImageField(upload_to='media/thumbnails/large')
    small_thumbnail = models.ImageField(upload_to='media/thumbnails/small')
    title = models.CharField(max_length=300)
    caption = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
