# Generated by Django 3.1.6 on 2021-02-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tijdschrijven', '0004_auto_20210207_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Personen',
            field=models.ManyToManyField(through='tijdschrijven.Abonnement', to='tijdschrijven.Persoon'),
        ),
    ]
