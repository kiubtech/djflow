from django.db.models import Sum
from django.db import models
from django.utils.translation import ugettext as _

from django.contrib.auth.models import User


class Account(models.Model):
    """
    Cuentas del usuario
    """
    created_by = models.ForeignKey(User, help_text=_("Usuario que ha creado la cuenta"))
    name = models.CharField(max_length=1000, verbose_name=_("Nombre"))
    description = models.TextField(max_length=1000, verbose_name=_("Descripción"), null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, help_text=_("Fecha de creación"))
    is_active = models.BooleanField(default=True, help_text=_("¿Se puede utilizar esta cuenta o está inactiva?"))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = _("Cuenta")
        verbose_name_plural = _("Cuentas")


class Category(models.Model):
    TYPE_OPTIONS = (
        (0, _("Egreso")),
        (1, _("Ingreso"))
    )

    name = models.CharField(max_length=500)
    type = models.IntegerField(choices=TYPE_OPTIONS, default=1)

    def __str__(self):
        if self.type == 0:
            return "[Egreso] {0}".format(self.name)
        else:
            return "[Ingreso] {0}".format(self.name)

    class Meta:
        ordering = ('name', )
        verbose_name = _("Categoría")
        verbose_name_plural = _("Categorías")


class Transaction(models.Model):
    """
    Registra los ingresos / egresos
    """

    created_by = models.ForeignKey(User, help_text=_("Usuario que ha creado la cuenta"))
    account = models.ForeignKey(Account, help_text=_("Cuenta a afectar"), verbose_name=_("Cuenta"))
    name = models.CharField(max_length=500, verbose_name=_("Descripción"))
    category = models.ForeignKey(Category, verbose_name=_("Categoría"))
    amount = models.DecimalField(decimal_places=2, max_digits=12, verbose_name=_("Monto"))
    date = models.DateField(help_text=_("Fecha del movimiento"), verbose_name=_("Fecha"))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-date",)
        verbose_name = _("Transacción")
        verbose_name_plural = _("Transacciones")


class TransactionComment(models.Model):
    transaction = models.ForeignKey(Transaction, verbose_name=_("Transacción"))
    created_by = models.ForeignKey(User, verbose_name=_("Usuario"))
    comment = models.TextField(max_length=1200, verbose_name=_("Comentario"))
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-timestamp', )
        verbose_name = _("Comentario de la transacción")
        verbose_name_plural = _("Comentarios de transacciones")
