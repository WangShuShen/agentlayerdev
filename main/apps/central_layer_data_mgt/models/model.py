from django.db import models

# Create your models here.
class Model(models.Model):
    """
        Model table
    """
    model_uid = models.UUIDField(
        max_length=36, blank=True, unique=True, primary_key=True)
    model_created_time = models.DateTimeField(
        blank=False)
    model_version = models.CharField(
        max_length=255, blank=False, default="1.0")
    model_file_path = models.TextField(
        blank=False, default="/")
    model_file_extension = models.CharField(
        max_length=255, blank=False, default="h5")
    model_access_token = models.CharField(
        max_length=255, blank=False, default="None")
    model_description = models.TextField(
        blank=False, default="Model description")
    model_published = models.BooleanField(
        blank=False, default=False)
    f_training_pipeline_uid = models.UUIDField(
        max_length=36, blank=True)
    f_application_uid = models.UUIDField(
        max_length=36, blank=True)
    
    class Meta:
        db_table = "model"
        managed = True