from django.db import models


class TODO(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
