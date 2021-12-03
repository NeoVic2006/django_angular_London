# Generated by Django 3.2.9 on 2021-12-03 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='first.device'),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('devices', models.ManyToManyField(to='first.Device')),
            ],
        ),
    ]