from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethon,ReadDetail



class BlogType(models.Model):
	type_name = models.CharField(max_length=15,verbose_name="分类")
	def __str__(self):
		return self.type_name
	class Meta:
		verbose_name_plural = "博客分类"

class Blog(models.Model,ReadNumExpandMethon):
	title = models.CharField(max_length=50,verbose_name="标题")
	blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING,verbose_name="分类")
	content = RichTextUploadingField(verbose_name="内容")
	author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name="作者")
	read_details = GenericRelation(ReadDetail)
	Created_time = models.DateTimeField(auto_now_add=True,verbose_name="发表时间")
	last_updated_time = models.DateTimeField(auto_now=True,verbose_name="最后更新时间")

	def __str__(self):
		return  "<Bolg:%s>" %self.title

	class Meta:
		ordering = ["-Created_time"]
		verbose_name_plural = "博客"


# class ReadNum(models.Model):
# 	read_num = models.IntegerField(default=0, verbose_name="阅读次数")
# 	blog = models.OneToOneField(Blog,on_delete=models.DO_NOTHING,verbose_name="标题")
# 	class Meta:
# 		verbose_name_plural = "阅读数量"