# Generated by Django 3.2.5 on 2022-02-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_email_state_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='state_field',
            field=models.BooleanField(default=False, null=True),
        ),
    ]