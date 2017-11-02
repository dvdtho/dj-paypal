# Generated by Django 1.11.4 on 2017-11-02 17:27
import datetime

from django.db import migrations, models
from django.utils.timezone import make_aware


TOKEN_DATE = make_aware(datetime.datetime(2063, 4, 5, 0, 0))


def update_end_of_period(apps, schema_editor):
	BillingAgreement = apps.get_model("djpaypal", "BillingAgreement")
	billing_agreements = BillingAgreement.objects.using(schema_editor.connection.alias)
	for ba in billing_agreements.filter(end_of_period=TOKEN_DATE):
		ba.end_of_period = ba.calculate_end_of_period()


class Migration(migrations.Migration):
	dependencies = [
		("djpaypal", "0001_initial"),
	]

	operations = [
		migrations.AddField(
			model_name="billingagreement",
			name="end_of_period",
			field=models.DateTimeField(db_index=True, default=TOKEN_DATE),
			preserve_default=False,
		),
		migrations.RunPython(update_end_of_period, None),
	]