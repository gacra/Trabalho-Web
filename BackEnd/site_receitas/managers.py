from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, usuario, password, **extra_fields):
        if not usuario:
            raise ValueError('Não há email')
        usuario = self.normalize_email(usuario)
        user = self.model(usuario=usuario, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(usuario, password, **extra_fields)

    def create_superuser(self, usuario, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(usuario, password, **extra_fields)