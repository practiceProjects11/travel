# Generated by Django 5.1.1 on 2024-10-12 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('admin', '0003_logentry_add_action_flag_choices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User_data',
        ),
    ]
