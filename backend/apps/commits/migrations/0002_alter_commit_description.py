# Generated by Django 3.2.5 on 2021-11-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='description',
            field=models.TextField(),
        ),
    ]