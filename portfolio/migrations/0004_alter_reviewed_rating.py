# Generated by Django 4.0 on 2022-02-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_reviewed_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewed',
            name='Rating',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]