# Generated by Django 3.0.4 on 2020-09-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasurehunt', '0008_score_ban'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerchecker',
            name='index',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]