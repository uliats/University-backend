from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from django.utils import timezone


class Service(models.Model):
    STATUS_CHOICES = (
        (1, 'Действует'),
        (2, 'Удалена'),
    )

    name = models.CharField(default="Печать", max_length=100, verbose_name="Название")
    description = models.TextField(default="Описание", max_length=500, verbose_name="Описание")
    expert = models.CharField(default="Эксперт", max_length=100, verbose_name="Зкспперт")

    status = models.IntegerField( choices=STATUS_CHOICES, default=1, verbose_name="Статус")
    image = models.ImageField(upload_to="services", default="services/default.jpg", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class CustomUserManager(BaseUserManager):
    def create_user(self, name, email, password="1234", **extra_fields):
        extra_fields.setdefault('name', name)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password="1234", **extra_fields):
        extra_fields.setdefault('is_moderator', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(name, email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    is_moderator = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Order(models.Model):
    STATUS_CHOICES = (
        (1, 'Введён'),
        (2, 'В работе'),
        (3, 'Завершён'),
        (4, 'Отменён'),
        (5, 'Удалён'),
    )



    services = models.ManyToManyField(Service, verbose_name="Работы", blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Статус")
    date_created = models.DateTimeField(default=datetime.now(tz=timezone.utc), verbose_name="Дата создания")
    date_formation = models.DateTimeField(verbose_name="Дата формирования", blank=True, null=True)
    date_complete = models.DateTimeField(verbose_name="Дата завершения", blank=True, null=True)

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Покупатель", related_name='owner', null=True)
    moderator = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, verbose_name="Модератор", related_name='moderator', blank=True, null=True)
    stage_readiness = models.IntegerField(verbose_name="Количество записей ",
                                                blank=True, null=True)

    def __str__(self):
        return "Заказ №" + str(self.pk)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ('-date_formation', )

class OrderServices(models.Model):
    service_id = models.ForeignKey(Service, models.DO_NOTHING)
    order_id = models.ForeignKey(Order, models.DO_NOTHING)
    stage_readiness = models.IntegerField(verbose_name="Количество записей ",
                                          blank=True, null=True)

    def __str__(self):
        return "м-м" + str(self.pk)

    class Meta:
        verbose_name = "м-м"
        verbose_name_plural = "м-м"