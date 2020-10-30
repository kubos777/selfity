from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from model_utils.models import TimeStampedModel
from .managers import UserManager
# Create your models here.

class Test(TimeStampedModel):
    name = models.CharField(
        'Test',
        max_length= 50
    )
    class Meta:
        verbose_name= 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.name

class User(AbstractBaseUser):
    telephone_regex = RegexValidator(regex=r'^(\d{10})$', message="Formato 10 dígitos máximo")
    telephone   = models.CharField(validators=[telephone_regex], max_length=17, unique=True)
    name        = models.CharField(max_length = 20, blank = True, null = True)
    first_login = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.telephone

    def get_full_name(self):
        return self.telephone

    def get_short_name(self):
        return self.telephone

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):

        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class Image(TimeStampedModel):
    MIMEType = models.CharField(
        'Tipo de imagen',
        max_length= 20,
        null= True
    )
    hashtag = models.CharField(
        'Nombre',
        max_length= 20,
        unique= True
    )
    coords = models.CharField(
        'Coordenadas',
        max_length= 500
    )
    file = models.ImageField(upload_to='images')
    thumbnail = models.ImageField(upload_to='thumbnails',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hashtag