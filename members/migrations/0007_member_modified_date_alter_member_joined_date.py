# Generated by Django 4.1.5 on 2023-01-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_member_joined_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='modified_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='joined_date',
            field=models.DateField(),
        ),
    ]
