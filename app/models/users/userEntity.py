from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import EmailValidator

class UserEntity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    email = models.EmailField(max_length=128, unique=True, validators=[EmailValidator()])

    # Adicione métodos para personalização
    def check_password(self, raw_password):
        return check_password(raw_password, self.user.password)

    def set_password(self, raw_password):
        self.user.password = make_password(raw_password)
        self.user.save()

    def __str__(self):
        return self.user.email
