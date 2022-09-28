# Generated by Django 3.2.14 on 2022-09-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_photo',
            field=models.CharField(choices=[('Cool', 'Cool'), ('Goth', 'Goth'), ('Serenity', 'Serenity'), ('Rock', 'Rock')], default='Cool', max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
