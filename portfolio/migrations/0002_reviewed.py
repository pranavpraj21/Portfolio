# Generated by Django 4.0 on 2022-02-20 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Relationship', models.CharField(default=' ', max_length=15)),
                ('Description', models.CharField(blank=True, max_length=100)),
                ('Rating', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3)),
                ('Social', models.URLField(blank=True)),
                ('Flag', models.BooleanField(default=False)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]