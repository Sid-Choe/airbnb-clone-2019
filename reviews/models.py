from audioop import avg
from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.PositiveIntegerField(default=5)
    communication = models.PositiveIntegerField(default=5)
    cleanliness = models.PositiveIntegerField(default=5)
    location = models.PositiveIntegerField(default=5)
    Check_in = models.PositiveIntegerField(default=5)
    vlaue = models.PositiveIntegerField(default=5)
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", related_name="reviews", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} {self.room}"

    def rating_average(self):
        avg = (self.accuracy + self.communication + self.cleanliness + self.location + self.Check_in + self.vlaue) / 6
        return round(avg, 2)