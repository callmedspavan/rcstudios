# Generated by Django 4.1.7 on 2023-03-03 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event_management', '0001_initial'),
        ('oneset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('streamLink', models.URLField(unique=True)),
                ('link', models.URLField(unique=True)),
                ('time', models.TimeField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnail/')),
                ('pcloudFileId', models.CharField(blank=True, max_length=300)),
                ('pubCode', models.CharField(max_length=1000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.event')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='portfolio/')),
                ('link', models.URLField(blank=True, unique=True)),
                ('pcloudFileId', models.CharField(blank=True, max_length=300)),
                ('pubCode', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oneset.category')),
            ],
        ),
        migrations.CreateModel(
            name='PlanQuerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management.customer')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manage_apk.plan')),
            ],
            options={
                'verbose_name': 'enquire',
                'verbose_name_plural': 'enquiries',
            },
        ),
        migrations.CreateModel(
            name='PlanAddon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_apk.plan')),
            ],
        ),
    ]
