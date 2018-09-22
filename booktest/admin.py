from django.contrib import admin
from booktest.models import BookInfo, HeroInfo


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'book_title', 'book_pub_date']


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hero_name', 'hero_gender', 'hero_content', 'hero_book']


# Register your models here.
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
