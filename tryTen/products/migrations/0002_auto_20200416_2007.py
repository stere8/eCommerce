# Generated by Django 3.0.5 on 2020-04-16 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
    ]
