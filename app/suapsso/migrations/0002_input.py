# Generated by Django 2.1 on 2018-08-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suapsso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.CharField(max_length=250)),
            ],
        ),
    ]
