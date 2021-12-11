# Generated by Django 3.2.9 on 2021-11-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome do Produto', max_length=80, unique=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=6)),
                ('section', models.CharField(help_text='Nome da seção', max_length=80, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
