# Generated by Django 3.0.4 on 2020-05-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('issues', models.IntegerField()),
            ],
        ),
    ]