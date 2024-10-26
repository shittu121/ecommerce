# Generated by Django 4.2.3 on 2023-08-07 22:15

from django.db import migrations, models
import django.db.models.deletion
import firstapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=firstapp.models.get_file_path)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to=firstapp.models.get_file_path)),
                ('small_description', models.TextField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('original_price', models.FloatField()),
                ('selling_price', models.FloatField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1=Hidden')),
                ('trending', models.BooleanField(default=False, help_text='0=default, 1=Trending')),
                ('tag', models.CharField(max_length=150)),
                ('meta_title', models.CharField(max_length=150)),
                ('meta_keywords', models.CharField(max_length=150)),
                ('meta_description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.category')),
            ],
        ),
    ]
