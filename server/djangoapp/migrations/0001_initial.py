import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                (
                    'name',
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False
                    )
                ),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                ('name', models.CharField(max_length=100)),
                (
                    'type',
                    models.CharField(
                        choices=[
                            ('SEDAN', 'Sedan'),
                            ('SUV', 'SUV'),
                            ('WAGON', 'Wagon')
                        ],
                        default='SUV',
                        max_length=100
                    )
                ),
                (
                    'year',
                    models.IntegerField(
                        default=2024,
                        validators=[
                            django.core.validators.MaxValueValidator(2024),
                            django.core.validators.MinValueValidator(2015)
                        ]
                    )
                ),
                (
                    'car_make',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='djangoapp.carmake'
                    )
                ),
            ],
        ),
    ]
