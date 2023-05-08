# Generated by Django 4.1.5 on 2023-05-08 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipo', '0001_initial'),
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tipo.tipo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='miniature',
            field=models.ImageField(upload_to='static/admin/img/'),
        ),
    ]