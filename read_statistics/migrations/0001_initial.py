# Generated by Django 2.2 on 2020-05-25 20:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0, verbose_name='阅读量')),
                ('object_id', models.PositiveIntegerField(verbose_name='博客id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType', verbose_name='博客')),
            ],
            options={
                'verbose_name_plural': '阅读量',
            },
        ),
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='日期')),
                ('read_num', models.IntegerField(default=0, verbose_name='阅读数量')),
                ('object_id', models.PositiveIntegerField(verbose_name='博客id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType', verbose_name='博客')),
            ],
            options={
                'verbose_name_plural': '每日阅读量',
            },
        ),
    ]
