# Generated by Django 3.2.3 on 2021-08-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_question2'),
    ]

    operations = [
        migrations.AddField(
            model_name='question2',
            name='Answer',
            field=models.CharField(max_length=1, null=True),
        ),
    ]