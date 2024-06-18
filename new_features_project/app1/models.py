from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    parent_template = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True, 
        related_name='child_templates'
    )

    def __str__(self):
        return self.name


class Narrative(models.Model):
    subject = models.CharField(max_length=100)
    age = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.subject