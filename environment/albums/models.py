from django.db import models

class Musician(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    instrument =models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Musicians'

class Album(models.Model):
    artist = models.ForeignKey('albums.Musician', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.artist.first_name
    
class Tag(models.Model):
    name =models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.title

