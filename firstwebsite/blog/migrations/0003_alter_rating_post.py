# Generated by Django 3.2.3 on 2021-06-07 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
