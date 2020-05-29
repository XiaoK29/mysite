from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0,verbose_name="阅读量")

    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING,verbose_name="博客")
    object_id = models.PositiveIntegerField(verbose_name="博客id")
    content_object = GenericForeignKey('content_type','object_id')

    class Meta:
        verbose_name_plural = "阅读量"

class ReadNumExpandMethon():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
            return 0


class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now,verbose_name="日期")
    read_num = models.IntegerField(default=0,verbose_name="阅读数量")

    content_type = models.ForeignKey(ContentType,on_delete=models.DO_NOTHING,verbose_name="博客")
    object_id = models.PositiveIntegerField(verbose_name="博客id")
    content_object = GenericForeignKey('content_type','object_id')
    class Meta:
        verbose_name_plural = "每日阅读量"















