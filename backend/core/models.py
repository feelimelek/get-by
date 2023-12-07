# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    cep = models.IntegerField(primary_key=True)  # The composite primary key (cep, state) found, that is not supported. The first column is selected.
    state = models.CharField()
    streetname = models.CharField(db_column='streetName')  # Field name made lowercase.
    city = models.CharField()

    class Meta:
        managed = False
        db_table = 'Address'
        unique_together = (('cep', 'state'),)

    def __str__(self):
        return f'{self.cep}' + self.state


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    senderid = models.IntegerField(db_column='senderId')  # Field name made lowercase.
    istipcreator = models.BooleanField(db_column='isTipCreator')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    text = models.CharField()
    tip_id = models.ForeignKey('Tip', models.DO_NOTHING, db_column='Tip_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comment'


class Emotion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'Emotion'


class EmotionTip(models.Model):
    emotion_id = models.OneToOneField(Emotion, models.DO_NOTHING, db_column='Emotion_id', primary_key=True)  # Field name made lowercase. The composite primary key (Emotion_id, Tip_id) found, that is not supported. The first column is selected.
    tip_id = models.ForeignKey('Tip', models.DO_NOTHING, db_column='Tip_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Emotion_Tip'
        unique_together = (('emotion_id', 'tip_id'),)


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField()
    last_name = models.IntegerField()
    email = models.CharField()
    points = models.IntegerField()
    password = models.CharField()
    specializationfield = models.CharField(db_column='specializationField', blank=True, null=True)  # Field name made lowercase.
    professional_id = models.IntegerField(blank=True, null=True)
    phonenumber = models.IntegerField(db_column='phoneNumber', blank=True, null=True)  # Field name made lowercase.
    isadmin = models.BooleanField(db_column='isAdmin', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class PersonEmotion(models.Model):
    person_id = models.OneToOneField(Person, models.DO_NOTHING, db_column='Person_id', primary_key=True)  # Field name made lowercase. The composite primary key (Person_id, Emotion_id) found, that is not supported. The first column is selected.
    emotion_id = models.ForeignKey(Emotion, models.DO_NOTHING, db_column='Emotion_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person_Emotion'
        unique_together = (('person_id', 'emotion_id'),)


class Selection(models.Model):
    id = models.IntegerField(primary_key=True)
    person_id = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_id')  # Field name made lowercase.
    tip_id = models.ForeignKey('Tip', models.DO_NOTHING, db_column='Tip_id')  # Field name made lowercase.
    task_id = models.ForeignKey('Task', models.DO_NOTHING, db_column='Task_id')  # Field name made lowercase.
    emotion_id = models.ForeignKey(Emotion, models.DO_NOTHING, db_column='Emotion_id')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    has_helped = models.BooleanField(db_column='hasHelped')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Selection'


class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    duedate = models.DateField(db_column='dueDate')  # Field name made lowercase.
    completed = models.BooleanField()
    emotion_id = models.ForeignKey(Emotion, models.DO_NOTHING, db_column='emotionId')  # Field name made lowercase.
    tip_id = models.ForeignKey('Tip', models.DO_NOTHING, db_column='Tip_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'


class Tip(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    description = models.TextField()
    points = models.IntegerField()
    cep = models.ForeignKey(Address, models.DO_NOTHING, db_column='cep')
    state = models.CharField()
    buildingnumber = models.IntegerField(db_column='buildingNumber', blank=True, null=True)  # Field name made lowercase.
    complement = models.CharField()
    country = models.CharField()
    validated = models.BooleanField()
    tip_creator_id = models.ForeignKey(Person, models.DO_NOTHING, db_column='tipCreatorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tip'


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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