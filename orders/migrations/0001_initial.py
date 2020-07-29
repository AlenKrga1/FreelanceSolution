# Generated by Django 3.0.8 on 2020-07-29 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import freelancesolution.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('product_type', models.CharField(choices=[(freelancesolution.enums.ProductType['ICON'], 'Icon'), (freelancesolution.enums.ProductType['LOGO'], 'Logo'), (freelancesolution.enums.ProductType['POSTER'], 'Poster')], max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
