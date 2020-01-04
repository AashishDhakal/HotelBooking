from django.db import models

class Slider(models.Model):
    heading_1 = models.CharField(max_length=100)
    heading_2 = models.CharField(max_length=100)
    bg_image = models.ImageField(upload_to="sliderimages")

    def __str__(self):
        return self.heading_1