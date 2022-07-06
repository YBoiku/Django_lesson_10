# Generated by Django 4.0.5 on 2022-07-06 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('humans', '0004_human_favorite_color_many_to_many_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperHuman',
            fields=[
                ('human_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='humans.human')),
                ('level', models.PositiveIntegerField(help_text='Level of power', verbose_name='Level')),
            ],
            bases=('humans.human',),
        ),
    ]
