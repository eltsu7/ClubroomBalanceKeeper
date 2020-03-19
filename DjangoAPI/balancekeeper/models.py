from django.db import models
from django.db.models import Sum
import uuid


class Category(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name    = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        ordering = ['name']

    @property
    def active(self):
        prods = Product.objects.filter(category=self.id)
        return any(prod.active == True for prod in prods)


class Product(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name        = models.CharField(max_length=50, blank=False)
    category    = models.ForeignKey(Category, related_name='products', on_delete=models.DO_NOTHING, null=False, default=uuid.uuid4)
    price       = models.IntegerField(blank=False)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        ordering = ['name']


class CbkUser(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(max_length=50, null=True, blank=True)
    telegram_id = models.BigIntegerField(unique=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "TgID: " + str(self.telegram_id)

    class Meta:
        db_table = 'cbk_user'
        ordering = ['name']

    @property
    def balance(self):
        balance = Transaction.objects.filter(cbk_user_id=self.id).aggregate(balance=Sum('product_id__price'))['balance']
        return balance or 0


class Transaction(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id  = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False, default=uuid.uuid4)
    cbk_user_id = models.ForeignKey(CbkUser, on_delete=models.DO_NOTHING, null=False, default=uuid.uuid4)
    date        = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=255, blank=True, null=False, editable=True)

    def __str__(self):
        return "{} ({} mc) for {}".format(self.product_id.name, self.product_id.price, self.cbk_user_id.name)

    class Meta:
        db_table = 'transaction'
        ordering = ['-date']