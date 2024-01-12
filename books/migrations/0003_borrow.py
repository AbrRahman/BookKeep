# Generated by Django 5.0 on 2024-01-12 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_deposit'),
        ('books', '0002_rename_categories_category_book_delete_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_time', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow', to='accounts.useraccount')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow', to='books.book')),
            ],
        ),
    ]
