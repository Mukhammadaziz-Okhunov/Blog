# Generated by Django 3.2.9 on 2021-12-24 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='media/')),
                ('maqola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog1.maqola')),
            ],
        ),
    ]