# Generated by Django 2.2.12 on 2022-05-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_multi_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='img_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
    ]