from django.db import models
from common.models import CommonModel

# lifestyle related posts

class LifestyleCategory(CommonModel):

    """lifestyle Category Definition"""

    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class LifestylePost(CommonModel):

    """lifestyle Post Model Definition"""

    title = models.CharField(max_length=255)
    payload = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey("lifestyles.lifestyleCategory", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.author} / {self.title}"