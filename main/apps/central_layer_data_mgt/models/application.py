from django.db import models

# Create your models here.
class Application(models.Model):
    """
        Application table
    """
    application_uid = models.UUIDField(
        max_length=36, blank=True, unique=True, primary_key=True)
    application_created_time = models.DateTimeField(
        max_length=255, blank=False)
    application_description = models.TextField(
        blank=False, default="Application description")
    application_name = models.CharField(
        max_length=255, blank=True, default="Application name")
    
    class Meta:
        db_table = "application"
        managed = True