## yeh new file banaye
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migration = True


    def create_user(self,  email,password = None, **extra_fields):
        if not email:
            raise ValueError("Email is Require")

        email  = self.normalize_email(email)
        user = self.model(email = email , **extra_fields)
        user.setpassword(password)
        user.save(using=self.db)
        return user
