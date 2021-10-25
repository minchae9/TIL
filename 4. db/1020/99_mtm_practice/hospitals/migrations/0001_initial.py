# Generated by Django 3.2.7 on 2021-10-20 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.TextField()),
                ('reserved_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(through='hospitals.Reservation', to='hospitals.Doctor'),
        ),
    ]