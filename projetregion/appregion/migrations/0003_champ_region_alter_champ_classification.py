# Generated by Django 4.0.3 on 2022-05-06 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appregion', '0002_champ'),
    ]

    operations = [
        migrations.AddField(
            model_name='champ',
            name='region',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appregion.region'),
        ),
        migrations.AlterField(
            model_name='champ',
            name='classification',
            field=models.TextField(),
        ),
    ]
