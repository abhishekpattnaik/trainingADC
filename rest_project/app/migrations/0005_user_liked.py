# Generated by Django 2.2.9 on 2020-01-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_url_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_liked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('liked_urls', models.ManyToManyField(to='app.test_model')),
            ],
        ),
    ]
