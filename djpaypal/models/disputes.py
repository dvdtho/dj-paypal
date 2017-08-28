from django.db import models

from .. import enums
from ..fields import CurrencyAmountField, JSONField
from .base import PaypalObject


class Dispute(PaypalObject):
	create_time = models.DateTimeField(editable=False)
	update_time = models.DateTimeField(null=True, editable=False)
	disputed_transactions = JSONField(editable=False)
	reason = models.CharField(
		max_length=39, choices=enums.DisputeReason.choices, editable=False
	)
	status = models.CharField(max_length=27, choices=enums.DisputeStatus.choices)
	dispute_amount = CurrencyAmountField(editable=False)
	dispute_outcome = JSONField(null=True, editable=False)
	messages = JSONField(null=True)
	seller_response_due_date = models.DateTimeField(null=True, editable=False)
	dispute_flow = models.CharField(
		max_length=25, choices=enums.DisputeFlow.choices, editable=False
	)