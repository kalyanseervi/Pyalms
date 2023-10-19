# Generated by Django 4.1.2 on 2023-10-17 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase2',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases_as_author', to='amsapp.book2'),
        ),
        migrations.AlterField(
            model_name='purchase2',
            name='book_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_as_title', to='amsapp.book2'),
        ),
        migrations.AlterField(
            model_name='purchase2',
            name='dealers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amsapp.dealers2'),
        ),
        migrations.AlterField(
            model_name='purchase2',
            name='totalprice',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
