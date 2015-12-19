# -*- coding: utf-8 -*-
from django.db import models


class Book(models.Model):
    name = models.CharField(u'書籍名', max_length=255)
    publisher = models.CharField(u'出版社', max_length=255, blank=True)
    page = models.IntegerField(u'ページ数', blank=True, default=0)

    def __unicode__(self):
        return self.name


class Impression(models.Model):
    book = models.ForeignKey(Book, verbose_name=u'書籍', related_name='impressions')
    comment = models.TextField(u'コメント', blank=True)

    def __unicode__(self):
        return self.comment