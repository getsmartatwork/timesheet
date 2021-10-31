from django.db import models

# Create your models here.


class AccountBaseModel(models.Model):
    organization_code = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now_add=True)
    remarks = models.CharField(max_length=400, blank=True, null=True)
    active_from = models.DateTimeField(auto_now=True)
    active_to = models.DateTimeField(blank=True, null=True) 

    class Meta:
        abstract = True


class Client(AccountBaseModel):
	client_name = models.CharField(max_length=100)

	def __str__(self):
		return "{}".format(self.client_name)


class Vendor(AccountBaseModel):
	vendor_name = models.CharField(max_length=100)

	def __str__(self):
		return "{}".format(self.vendor_name)