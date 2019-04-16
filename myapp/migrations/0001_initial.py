# Generated by Django 2.1.7 on 2019-04-11 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_num', models.IntegerField()),
                ('rep_num', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.workout'),
        ),
    ]