# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('MiningsAppCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MiningsAppCustomuser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=254)
    name = models.CharField(max_length=30)
    is_moderator = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'minings_app_customuser'


class MiningsAppCustomuserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(MiningsAppCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'minings_app_customuser_groups'
        unique_together = (('customuser', 'group'),)


class MiningsAppCustomuserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    customuser = models.ForeignKey(MiningsAppCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'minings_app_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class MiningsAppOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    # execution_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    date_created = models.DateTimeField()
    date_formation = models.DateTimeField(blank=True, null=True)
    date_complete = models.DateTimeField(blank=True, null=True)
    moderator = models.ForeignKey(MiningsAppCustomuser, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(MiningsAppCustomuser, models.DO_NOTHING, related_name='miningsapporder_owner_set', blank=True, null=True)
    stage_readiness = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minings_app_order'


class MiningsAppOrderServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    order = models.ForeignKey(MiningsAppOrder, models.DO_NOTHING)
    service = models.ForeignKey('MiningsAppService', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'minings_app_order_services'
        unique_together = (('order', 'service'),)


class MiningsAppService(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField()
    image = models.CharField(max_length=100)
    expert = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'minings_app_service'
