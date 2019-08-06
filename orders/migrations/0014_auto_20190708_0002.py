# Generated by Django 2.2 on 2019-07-07 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_order_buktipembayaran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buktipembayaran',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buktiPembayaran',
            field=models.FileField(blank=True, null=True, upload_to='bukti_pembayaran/'),
        ),
    ]