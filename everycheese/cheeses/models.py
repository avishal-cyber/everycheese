from django.db import models

from  autoslug import AutoSlugField

from  model_utils.models import TimeStampedModel

class Cheese(TimeStampedModel):
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "Soft", "soft"
        SEMI_SOFT = "semi-soft", "Semi-soft"
        SEMI_HARD = "Semi-hard", "semi-hard"
        HARD = "hard", "Hard"

    def __str__(self):
        return self.name
    
    name = models.CharField("Name of Cheese", max_length = 255)
    slug = AutoSlugField("Cheese Adress", unique = True, 
    always_update = False, populate_from = "name")
    description = models.TextField("Description", blank = True)
    firmness = models.CharField("Firmness", max_length=20, 
    choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    
