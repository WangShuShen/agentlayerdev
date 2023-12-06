from django.db import models
from main.apps.central_layer_data_mgt.models.model import Model

# Create your models here.
class ModelPerformance(models.Model):
    """
        Model performance table
    """
    model_performance_uid = models.UUIDField(
        max_length=36, blank=True, unique=True, primary_key=True)
    model_performance_created_time  = models.DateTimeField(
        max_length=255, blank=False)
    model_performance_matrice = models.CharField(
        max_length=255, blank=False, default="None")
    model_performance_value = models.CharField(
        max_length=255, blank=False, default="None")
    f_model_uid = models.ForeignKey(
        Model, blank=True, on_delete=models.CASCADE, to_field='model_uid')
    
    class Meta:
        db_table = "model_performance"
        managed = True