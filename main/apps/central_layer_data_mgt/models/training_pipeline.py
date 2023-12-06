from django.db import models
from main.apps.central_layer_data_mgt.models.application import Application

# Create your models here.
class TrainingPipeling(models.Model):
    """
        Training pipeline table
    """
    training_pipeling_uid = models.UUIDField(
        max_length=36, blank=True, unique=True, primary_key=True)
    training_pipeling_created_time = models.DateTimeField(
        max_length=255, blank=False)
    training_pipeling_name = models.CharField(
        max_length=255, blank=True, default="TrainingPipeline name")
    training_pipeling_description = models.TextField(
        blank=False, default="TrainingPipeline description")
    f_application_uid = models.ForeignKey(
        Application, blank=True, on_delete=models.CASCADE, to_field='application_uid')
    
    class Meta:
        db_table = "training_pipeline"
        managed = True