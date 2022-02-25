from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("event:event", kwargs={"event": self.slug})