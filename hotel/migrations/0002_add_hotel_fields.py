from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='location',
            field=models.CharField(max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2),
        ),
        migrations.AddField(
            model_name='hotel',
            name='number_of_rooms',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='phone',
            field=models.CharField(max_length=20, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='email',
            field=models.EmailField(max_length=254, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='main_image',
            field=models.ImageField(upload_to='hotel_images/', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]


