# Generated by Django 4.1.7 on 2023-03-18 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0007_book_mybook'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]
