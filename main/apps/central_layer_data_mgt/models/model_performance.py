from django.db import models

# Create your models here.
class ModelPerformance(models.Model):
    """
        Model performance table
    """
    model_performance_uid = models.UUIDField(
        max_length=36, blank=True, unique=True, primary_key=True)
    model_performance_created_time  = models.DateTimeField(
        blank=False)
    model_performance_matrice = models.CharField(
        max_length=255, blank=False, default="None")
    model_performance_value = models.CharField(
        max_length=255, blank=False, default="None")
    f_model_uid = models.UUIDField(
        max_length=36, blank=True)
    
    class Meta:
        db_table = "model_performance"
        managed = True