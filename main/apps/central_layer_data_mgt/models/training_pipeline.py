from django.db import models

# Create your models here.
class TrainingPipeline(models.Model):
    """
        Training pipeline table
    """
    training_pipeline_uid = models.UUIDField(
        max_length=36, blank=True, unique=True, primary_key=True)
    training_pipeline_created_time = models.DateTimeField(
        blank=False)
    training_pipeline_name = models.CharField(
        max_length=255, blank=True, default="TrainingPipeline name")
    training_pipeline_description = models.TextField(
        blank=False, default="TrainingPipeline description")
    f_application_uid = models.UUIDField(
        max_length=36, blank=True)
    
    class Meta:
        db_table = "training_pipeline"
        managed = True