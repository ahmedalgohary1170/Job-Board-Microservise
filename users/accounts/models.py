from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager





class CustomUserManager(BaseUserManager):
    '''  used to create user : password , create superuser '''

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError('the email field is required ...')
    
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user


    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        return self.create_user(email,password,**extra_fields)



class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='users/',blank=True,null=True)
    

    USERNAME_FIELD = 'email' # login with email
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return self.email


