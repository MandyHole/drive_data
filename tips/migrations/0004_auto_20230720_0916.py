# Generated by Django 3.2.19 on 2023-07-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_rename_author_tip_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='ability',
            field=models.CharField(choices=[('beginner', 'Beginner+'), ('intermediate', 'Intermediate+'), ('advanced', 'Advanced')], max_length=32, verbose_name='Recommended ability level'),
        ),
        migrations.AlterField(
            model_name='tip',
            name='category',
            field=models.CharField(choices=[('drive_pdf', 'Drive/PDFs'), ('sheets', 'Sheets'), ('slides', 'Slides'), ('docs', 'Docs'), ('forms', 'Forms')], max_length=32, verbose_name='Primary category of tip'),
        ),
        migrations.AlterField(
            model_name='tip',
            name='screenshot',
            field=models.ImageField(blank=True, default='../screenshot-default.jpg', upload_to='GetDriveing/', verbose_name='Upload a screenshot if applicable'),
        ),
        migrations.AlterField(
            model_name='tip',
            name='tip_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tip',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
