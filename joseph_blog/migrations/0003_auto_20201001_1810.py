# Generated by Django 3.1.1 on 2020-10-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph_blog', '0002_auto_20201001_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, max_length=100, verbose_name='Summary'),
        ),
    ]
