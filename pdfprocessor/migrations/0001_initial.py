# Generated by Django 5.0.3 on 2024-03-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('content', models.TextField()),
                ('nouns', models.TextField()),
                ('verbs', models.TextField()),
            ],
        ),
    ]