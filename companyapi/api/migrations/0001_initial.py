# Generated by Django 5.1.2 on 2024-10-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile phone', 'Mobile phone')], max_length=200)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('about', models.TextField()),
            ],
        ),
    ]