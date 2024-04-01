from django.db import models
from common.models import CommonModel

# Business related posts

class BusinessCategory(CommonModel):

    """Business Category Definition"""

    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class BusinessPost(CommonModel):

    """Business Post Model Definition"""

    title = models.CharField(max_length=255)
    payload = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey("businesses.BusinessCategory", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.author} / {self.title}"