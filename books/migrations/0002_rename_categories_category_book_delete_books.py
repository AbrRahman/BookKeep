# Generated by Django 5.0 on 2024-01-11 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('descriptions', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
                ('borrowing_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
