from django.db import models

class Tender(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to='tenders/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    recommendation_score = models.FloatField(null=True, blank=True)
    generated_response = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
