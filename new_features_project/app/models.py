from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    dependent_templates = models.ManyToManyField(
        'self',
        blank=True,
        related_name='parent_templates',
        symmetrical=False
    )

    def __str__(self):
        return self.name
