# Generated by Django 3.0.3 on 2020-02-12 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0002_auto_20200210_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='hobbies',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, help_text='The date and time this page was created. Automatically generated when the model saves.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hobbies',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='The date and time this page was updated. Automatically generated when the model updates.'),
        ),
        migrations.AddField(
            model_name='hobbies',
            name='slug',
            field=models.CharField(blank=True, default='Slug-of-Hobby', editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=100),
        ),
        migrations.AlterField(
            model_name='attend',
            name='choice',
            field=models.CharField(default='Attending', max_length=200),
        ),
        migrations.AlterField(
            model_name='hobbies',
            name='name',
            field=models.CharField(default='Name of Hobby', help_text='Name of your hobby.', max_length=100, unique=True),
        ),
    ]
