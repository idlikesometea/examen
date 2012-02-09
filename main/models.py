from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField('Tag')

    def __unicode__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    birth_date = models.DateField('Birth Date (YYYY-MM-DD)')

    def __unicode__(self):
        return self.last_name


class Comment(models.Model):
    article = models.ForeignKey('Article')
    nickname = models.CharField(max_length=15)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.nickname


class Tag(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name
