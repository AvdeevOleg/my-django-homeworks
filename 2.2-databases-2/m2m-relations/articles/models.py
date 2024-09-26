from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default="", null=True, blank=True)
    published_at = models.DateTimeField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='articles')
    tags = models.ManyToManyField(Tag, through='Scope', related_name='articles')

    def __str__(self):
        return self.title

class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)


