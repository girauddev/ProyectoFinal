# Generated by Django 4.0.3 on 2022-05-04 06:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='mensaje',
            field=ckeditor.fields.RichTextField(verbose_name='Mensaje'),
        ),
    ]
