# Generated by Django 4.0.5 on 2022-06-10 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_section_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
