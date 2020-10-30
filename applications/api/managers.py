from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, telephone, password=None, is_staff=False, is_active=True, is_admin=False):
        if not telephone:
            raise ValueError('El usuario debe tener teléfono')
        if not password:
            raise ValueError('El usuario debe tener contraseña')

        user_obj = self.model(
            telephone=telephone
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, telephone, password=None):
        user = self.create_user(
            telephone,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, telephone, password=None):
        user = self.create_user(
            telephone,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user