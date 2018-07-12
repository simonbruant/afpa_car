from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Les utilisateurs doivent avoir une adresse email.")
        if not password:
            raise ValueError("Les utilisateurs doivent avoir un mot de passe.")
        if not username:
            raise ValueError("Les utilisateurs doivent avoir un pseudo.")
        if not first_name:
            raise ValueError("Les utilisateurs doivent avoir prénom.")
        if not last_name:
            raise ValueError("Les utilisateurs doivent avoir un nom.")

        user_obj = self.model(
            email = self.normalize_email(email) # lower le nom de domaine
        )
        user_obj.set_password(password) #change user password
        user_obj.username = username
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email,
            username,
            first_name,
            last_name,
            password = password,
            is_staff = True,
        )
        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email,
            username,
            first_name,
            last_name,
            password = password,
            is_staff = True,
            is_admin = True,
        )
        return user
