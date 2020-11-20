# Generated by Django 3.1.3 on 2020-11-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201116_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quiztakers',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quiztakers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='response',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.RemoveField(
            model_name='response',
            name='quiztaker',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='course',
            field=models.ManyToManyField(to='blog.Post'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizTakers',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
