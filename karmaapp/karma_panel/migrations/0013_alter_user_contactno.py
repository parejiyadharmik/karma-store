# Generated by Django 3.2.5 on 2021-09-19 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma_panel', '0012_alter_user_contactno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contactno',
            field=models.IntegerField(),
        ),
    ]