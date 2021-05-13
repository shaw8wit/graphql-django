# Generated by Django 3.2.2 on 2021-05-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subcode', models.CharField(max_length=10)),
                ('students', models.ManyToManyField(to='api.Student')),
                ('teachers', models.ManyToManyField(to='api.Teacher')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='student',
            name='mentor',
            field=models.ManyToManyField(to='api.Teacher'),
        ),
    ]