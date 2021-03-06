# Generated by Django 2.2 on 2020-05-25 20:10

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import read_statistics.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15, verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('Created_time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('last_updated_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('blog_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.BlogType', verbose_name='分类')),
            ],
            options={
                'verbose_name_plural': '博客',
                'ordering': ['-Created_time'],
            },
            bases=(models.Model, read_statistics.models.ReadNumExpandMethon),
        ),
    ]
