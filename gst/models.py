from django.db import models


class Search(models.Model):
    hsn_code = models.IntegerField()
    hsn_descriptions = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.hsn_code}  {self.hsn_descriptions}'

