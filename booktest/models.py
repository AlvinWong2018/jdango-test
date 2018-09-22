from django.db import models


# Create your models here.
class BookInfo(models.Model):
    book_title = models.CharField(max_length=20)
    book_pub_date = models.DateField()

    def __str__(self):
        return str(self.pk)


class HeroInfo(models.Model):
    hero_name = models.CharField(max_length=20)
    hero_gender = models.BooleanField(default=True)
    hero_content = models.CharField(max_length=100)
    hero_book = models.ForeignKey(BookInfo)

    def __str__(self):
        return str(self.pk)
