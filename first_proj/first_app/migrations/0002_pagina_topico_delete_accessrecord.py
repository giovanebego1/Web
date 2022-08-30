# Generated by Django 4.1 on 2022-08-30 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.webpage')),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=264, unique=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.webpage')),
            ],
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
    ]
