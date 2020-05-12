# Generated by Django 2.1.5 on 2019-03-15 10:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0046_auto_20190206_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='breeddescription',
            name='br_descript_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Br descript'),
        ),
        migrations.AddField(
            model_name='breeddescription',
            name='br_descript_et',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Br descript'),
        ),
        migrations.AddField(
            model_name='breeddescription',
            name='br_descript_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Br descript'),
        ),
        migrations.AlterField(
            model_name='breeddescription',
            name='br_descript',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Br descript'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='adress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Adress'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='e_mail',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='E mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='kennel',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Kennel'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='owner1',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Owner1'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='owner2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Owner2'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='content',
            name='home_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Home text'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='dog_sex',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Dog sex'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='home_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Home name'),
        ),
        migrations.AlterField(
            model_name='dog',
            name='pedigree',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Pedigree'),
        ),
        migrations.AlterField(
            model_name='link',
            name='banner',
            field=models.TextField(blank=True, null=True, verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='mybanner',
            name='html_text',
            field=models.TextField(blank=True, null=True, verbose_name='Html text'),
        ),
        migrations.AlterField(
            model_name='mybanner',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='new',
            name='news_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='News text'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='puppy',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='puppy',
            name='p_sex',
            field=models.CharField(blank=True, choices=[('Boy', 'Boy'), ('Girl', 'Girl')], max_length=4, null=True, verbose_name='P sex'),
        ),
        migrations.AlterField(
            model_name='puppy',
            name='status',
            field=models.CharField(blank=True, choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Sold', 'Sold')], max_length=9, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='showresult',
            name='show_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Show id'),
        ),
        migrations.AlterField(
            model_name='showresult',
            name='show_judge',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Show judge'),
        ),
        migrations.AlterField(
            model_name='showresult',
            name='show_locale',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Show locale'),
        ),
        migrations.AlterField(
            model_name='showresult',
            name='show_result',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Show result'),
        ),
    ]