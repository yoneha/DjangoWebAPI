# Generated by Django 3.0.2 on 2020-01-23 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', '下書き'), ('public', '公開中')], default='draft', max_length=8)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='mail',
            field=models.EmailField(default='test@aaa.bbb', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=32),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='restapiapp.User'),
        ),
    ]