# Generated by Django 3.2.6 on 2021-09-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpanel', '0002_adminfile_adminlist_studentrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLearning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, unique=True)),
                ('video_url', models.CharField(default='#', max_length=350, unique=True)),
                ('is_published', models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
