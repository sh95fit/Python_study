# Generated by Django 4.1.4 on 2023-01-13 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_shortenedurls_expired_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortenedurls',
            name='click',
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=15)),
                ('web_browser', models.CharField(max_length=15)),
                ('device', models.CharField(choices=[('PC', 'Pc'), ('mobile', 'Mobile'), ('tablet', 'Tablet')], max_length=6)),
                ('device_os', models.CharField(max_length=30)),
                ('country_code', models.CharField(default='XX', max_length=2)),
                ('country_name', models.CharField(default='UNKNOWN', max_length=100)),
                ('shortened_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener.shortenedurls')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
