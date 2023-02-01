from django.db import models

# Create your models here.


from django.utils import timezone



"""
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
"""


class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  #joined_date = models.DateField(null=True)
  joined_date = models.DateField(auto_now_add=False)
  modified_date = models.DateField(null=True)

#
  def __str__(self):
    return f"{self.firstname} {self.lastname}"

  def that_joined_recently(self):
    return self.joined_date >= timezone.now() - date.timedelta(days=1)
  
 