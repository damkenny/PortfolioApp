# Generated by Django 2.2 on 2020-02-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(default='img/client.png', upload_to='img'),
        ),
    ]
