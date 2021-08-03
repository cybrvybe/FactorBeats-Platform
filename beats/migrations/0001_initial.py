# Generated by Django 3.2.3 on 2021-07-20 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('bpm', models.FloatField(blank=True, null=True)),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now=True, null=True)),
                ('producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='artists.artist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstrumentalCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('instrumentals', models.ManyToManyField(blank=True, to='beats.Instrumental')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]