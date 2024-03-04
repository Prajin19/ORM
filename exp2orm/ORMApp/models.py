from django.db import models
from django.contrib import admin
class Books_DB(models.Model):
    bklino=models.IntegerField(primary_key="bklino");
    bookname=models.CharField(max_length=30);
    author=models.CharField(max_length=20);
    publ=models.CharField(max_length=20);
    pgs=models.IntegerField();
    price=models.IntegerField();
class Books_DBAdmin(admin.ModelAdmin):
    list_display=("bklino","bookname","author","publ","pgs","price");
