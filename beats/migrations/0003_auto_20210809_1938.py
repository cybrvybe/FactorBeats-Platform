# Generated by Django 3.2.3 on 2021-08-10 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0002_artist_bio'),
        ('beats', '0002_instrumental_img_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumental',
            name='producer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='artists.artist'),
        ),
        migrations.AlterField(
            model_name='instrumentalcollection',
            name='instrumentals',
            field=models.ManyToManyField(blank=True, related_name='_beats_instrumentalcollection_instrumentals_+', to='beats.Instrumental'),
        ),
    ]
