from django.db import models

class Miningservices(models.Model):
    nameservice = models.CharField(max_length=100)
    description = models.TextField()
    expert = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    idservice = models.AutoField(primary_key=True)

    # Новое поле для отслеживания статуса
    mining_status = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.nameservice

    class Meta:
        managed = False
        db_table = 'miningservices'

class Users(models.Model):
    iduser = models.AutoField(primary_key=True)
    username = models.TextField(max_length=30)
    email = models.TextField(max_length=30)
    password = models.TextField(max_length=30)

    class Meta:
        managed = False
        db_table = 'users'
        app_label = 'bmstu_lab'  # Change 'postgres' to the actual app label


class RequestService(models.Model):
        requestid = models.IntegerField()
        serviceid = models.IntegerField()

        class Meta:
            managed = False
            db_table = 'request_service'


class Requests(models.Model):
        idrequest = models.IntegerField(primary_key=True)
        status_field = models.TextField(
            db_column='status')  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
        created_date = models.DateField(blank=True, null=True)
        formation_date_field = models.DateField(db_column='formation_date ', blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
        completion_date_field = models.DateField(db_column='completion_date ', blank=True,
                                                 null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
        creatorid_field = models.IntegerField(db_column='creatorid ', blank=True,
                                              null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
        moderatorid_field = models.IntegerField(db_column='moderatorid ', blank=True,
                                                null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

        class Meta:
            managed = False
            db_table = 'requests'






        #from django.db import models
#
# class Miningservices(models.Model):
#     idservice = models.AutoField(primary_key=True)
#     nameservice = models.CharField(max_length=30)
#     expert = models.CharField(max_length=50)  # Замените тип данных на подходящий
#     description = models.TextField()  # Замените тип данных на подходящий
#     image = models.ImageField(upload_to='media/miningservice_images/')  # Поле для хранения изображения

