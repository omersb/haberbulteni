# Generated by Django 4.2.1 on 2023-06-01 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0003_alter_makale_yayımlanma_tarihi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gazeteci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=120)),
                ('soyisim', models.CharField(max_length=120)),
                ('biyografi', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='makale',
            name='yazar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='makaleler', to='haberler.gazeteci'),
        ),
    ]
