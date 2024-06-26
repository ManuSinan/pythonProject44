# Generated by Django 5.0.3 on 2024-04-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
