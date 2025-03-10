# Generated by Django 4.2.19 on 2025-03-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
