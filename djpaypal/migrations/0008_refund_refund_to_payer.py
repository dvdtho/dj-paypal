# Generated by Django 2.1.2 on 2018-11-18 22:14

from django.db import migrations
import djpaypal.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djpaypal', '0007_sale_invoice_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='refund_to_payer',
            field=djpaypal.fields.CurrencyAmountField(editable=False, null=True),
        ),
    ]