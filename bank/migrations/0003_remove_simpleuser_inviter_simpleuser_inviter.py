# Generated by Django 4.1.5 on 2023-01-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_alter_simpleuser_inviter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simpleuser',
            name='inviter',
        ),
        migrations.AddField(
            model_name='simpleuser',
            name='inviter',
            field=models.ManyToManyField(to='bank.simpleuser'),
        ),
    ]
