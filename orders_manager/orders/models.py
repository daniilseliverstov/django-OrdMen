from django.db import models


ORDER_STATUS = (
    ("accepted", "Принят"),
    ("in_progress", "В работе"),
    ("documents", "Документы"),
    ("suspended", "Приостановлен"),
    ("reschedule", "Перенос"),
    ("ready", "Готово"),
)


class Order(models.Model):

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    order_number = models.CharField(max_length=20, verbose_name="Номер заказа")
    status = models.CharField(
        choices=ORDER_STATUS,
        max_length=20,
        default="accepted",
        verbose_name="Статус заказа",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Изменен")
    month = models.IntegerField(max_length=10, verbose_name="Месяц", null=True)
    week = models.IntegerField(verbose_name="Неделя", null=True)
    manager = models.CharField(
        max_length=20,
        verbose_name="Менеджер. Создать отдельную модель в приложении Пользователей",
    )
    customer = models.CharField(
        max_length=20,
        verbose_name="Заказчик. Создать отдельную модель в приложении Пользователей",
    )
    technologist = models.CharField(
        max_length=20,
        verbose_name="Технолог. Создать отдельную модель в приложении Пользователей",
        blank=True,
    )
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Масса", default=0
    )
    package = models.IntegerField(
        verbose_name="Количество упаковок", null=True, default=0
    )

    mdf = models.BooleanField(verbose_name="МДФ", default=False)
    furniture = models.BooleanField(verbose_name="Фурнитура", default=False)
    grass = models.BooleanField(verbose_name="Стекло", default=False)
    cnc = models.BooleanField(verbose_name="ЧПУ", default=False)

    materials = models.CharField(
        verbose_name="Материалы. Создать отдельную модель", blank=True
    )

    quadrature = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name="Квадратура", null=True, default=0
    )
    serial = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Серийная продукция",
        null=True,
        default=0,
    )
    portal = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Каминные порталы",
        null=True,
        default=0,
    )
    reclamation = models.CharField(
        max_length=250, verbose_name="Причина рекламации", blank=True
    )

    def __str__(self) -> str:
        return f"{self.order_number}"
