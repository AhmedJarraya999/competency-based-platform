from django.db import models

# Create your models here.
class StudyPlan(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='study_plans/')
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    class Meta:
        app_label = 'myapp'
    