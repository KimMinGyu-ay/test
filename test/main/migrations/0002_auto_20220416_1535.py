# Generated by Django 3.2 on 2022-04-16 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=5)),
                ('user', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=13)),
                ('e_mail', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='모델클래스',
        ),
    ]
