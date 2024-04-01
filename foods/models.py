from django.db import models
from common.models import CommonModel

# Food related posts

class FoodCategory(CommonModel):

    """Food Category Definition"""

    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class FoodPost(CommonModel):

    """Food Post Model Definition"""

    title = models.CharField(max_length=255)
    payload = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey("foods.FoodCategory", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.author} / {self.title}"