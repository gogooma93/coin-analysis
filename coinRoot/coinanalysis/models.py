from email.policy import default
from django.db import models
from django.utils.timezone import now

# Create your models here.
class BitcoinER(models.Model):
    date = models.DateField(auto_now=False)
    open = models.IntegerField(default=0)
    high= models.IntegerField(default=0)
    low = models.IntegerField(default=0)
    close = models.IntegerField(default=0)
    volume = models.FloatField(default=0.0)
    value = models.FloatField(default=0.0)
    won = models.FloatField(default=0.0)

class QnA(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    writeDate = models.DateTimeField(default=now, editable=False)
    writeID = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title