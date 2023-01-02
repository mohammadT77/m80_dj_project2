from django.db import models


# Create your models here.
class SimpleUser(models.Model):  # NOT django USER!
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)

    invite_code = models.CharField(max_length=10)  # Aws123A
    inviter = models.ManyToManyField('self')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BankAccount(models.Model):
    serial = models.CharField(max_length=30)
    users = models.ManyToManyField(SimpleUser)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.serial}: {list(self.users.all())}"


class BankCard(models.Model):
    serial = models.CharField(max_length=16)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.RESTRICT)
    user = models.ForeignKey(SimpleUser, on_delete=models.RESTRICT)
    cvv2 = models.CharField(max_length=4)
    expire_date = models.DateField()
    ...


class CardTransaction(models.Model):
    pass
