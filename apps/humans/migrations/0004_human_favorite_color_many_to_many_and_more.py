# Generated by Django 4.0.5 on 2022-07-06 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('humans', '0003_color_human_favorite_color_by_foreign_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='favorite_color_many_to_many',
            field=models.ManyToManyField(related_name='humans_related_by_many_to_many', to='humans.color'),
        ),
        migrations.AlterField(
            model_name='human',
            name='favorite_color_by_foreign_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='humans_related_by_foreign_key', to='humans.color'),
        ),
    ]