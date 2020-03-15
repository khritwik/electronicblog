# Generated by Django 3.0.3 on 2020-03-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200303_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='image2',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='article',
            name='l_heading',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='l_heading_text',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='quote',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='quote_name',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='s_heading',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='s_heading_text',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='tag_1',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='tag_2',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='tag_3',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='article',
            name='text2',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_date',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=2000),
        ),
    ]