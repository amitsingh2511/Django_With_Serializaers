from django.db import models

# DB Models For Compliance
class Compliance(models.Model):
    name = models.CharField(max_length=255)

# DB Models For Application
class Application(models.Model):
    name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    compliance = models.ForeignKey(Compliance, on_delete=models.CASCADE, related_name='applications')
