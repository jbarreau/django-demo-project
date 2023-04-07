# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings

class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'categories'


class Ranges(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'ranges'


class BookRange(models.Model):
    id = models.BigAutoField(primary_key=True)

    book = models.ForeignKey('Books', models.CASCADE)
    range = models.ForeignKey('Ranges', models.CASCADE)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'book_range'


class Books(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    comment = models.TextField()
    difficulty = models.CharField(max_length=255)
    amount = models.FloatField()
    active = models.BooleanField()
    options = models.JSONField()
    other = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey('Categories', models.CASCADE)
    ranges = models.ManyToManyField('Ranges', through="BookRange")

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'books'


class Editors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    book = models.OneToOneField('Books', models.CASCADE)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'editors'


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    book = models.ForeignKey('Books', models.CASCADE)
    user = models.ForeignKey('Users', models.CASCADE)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'comments'


class Advertisements(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    book = models.OneToOneField('Books', models.CASCADE)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'advertisements'


class Movies(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    book = models.ForeignKey(Books, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'movies'


# ###########


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    author = models.ForeignKey('Authors', models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'users'


class Authors(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    book = models.ForeignKey('Books', models.CASCADE)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'authors'


# ###########


class Bookstores(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    company = models.ForeignKey('Companies', models.DO_NOTHING)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'bookstores'


class Companies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    book = models.ForeignKey('Books', models.CASCADE)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'companies'


# ###########


class Buys(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'buys'


class Buyables(models.Model):
    id = models.BigAutoField(primary_key=True)

    # polymorph foreign key
    buyable_id = models.IntegerField()
    buyable_type = models.CharField(max_length=255)

    buy = models.ForeignKey('Buys', models.DO_NOTHING)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'buyables'


# see later :


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    token = models.UUIDField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivery_hour = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'products'


class Tags(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    # polymorph foreign key
    taggable_type = models.CharField(max_length=255)
    taggable_id = models.BigIntegerField()

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'tags'


class Sequels(models.Model):
    id = models.BigAutoField(primary_key=True)
    label = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    # polymorph foreign key
    sequelable_type = models.CharField(max_length=255, blank=True, null=True)
    sequelable_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'sequels'


# #####" dunno

class Images(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    imageable_type = models.CharField(max_length=255)
    imageable_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_MODELS
        db_table = 'images'


# #######  laravel framework related
# class PasswordResets(models.Model):
#     email = models.CharField(max_length=255)
#     token = models.CharField(max_length=255)
#     created_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = settings.MANAGE_MODELS
#         db_table = 'password_resets'


# class PersonalAccessTokens(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     tokenable_type = models.CharField(max_length=255)
#     tokenable_id = models.BigIntegerField()
#     name = models.CharField(max_length=255)
#     token = models.CharField(unique=True, max_length=64)
#     abilities = models.TextField(blank=True, null=True)
#     last_used_at = models.DateTimeField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = settings.MANAGE_MODELS
#         db_table = 'personal_access_tokens'


# class Migrations(models.Model):
#     migration = models.CharField(max_length=255)
#     batch = models.IntegerField()

#     class Meta:
#         managed = settings.MANAGE_MODELS
#         db_table = 'migrations'


# class FailedJobs(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     uuid = models.CharField(unique=True, max_length=255)
#     connection = models.TextField()
#     queue = models.TextField()
#     payload = models.TextField()
#     exception = models.TextField()
#     failed_at = models.DateTimeField()

#     class Meta:
#         managed = settings.MANAGE_MODELS
#         db_table = 'failed_jobs'