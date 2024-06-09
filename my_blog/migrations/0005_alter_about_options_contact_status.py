# Generated by Django 5.0.6 on 2024-06-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_about_contact_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('received', 'Received'), ('pending', 'Pending'), ('solved', 'Solved'), ('rejected', 'Rejected')], default='received', max_length=10),
        ),
    ]
