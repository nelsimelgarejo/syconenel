# Generated by Django 3.2.8 on 2021-10-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentirsebien', '0003_alter_dataunfv_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataunfv',
            name='activado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dataunfv',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]