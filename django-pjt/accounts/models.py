from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from banks.models import SavingProducts, DepositProducts

class CustomAccountAdapter(DefaultAccountAdapter):
     def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        age = data.get("age")
        asset = data.get("asset")
        salary = data.get("salary")
        # nickname 데이터 가져오기
        nickname = data.get('nickname')

        user_email(user, email)
        user_username(user, username)
        
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, 'nickname', nickname)
        if age:
            user.age = age
        if asset:
            user.asset = asset
        if salary:
            user.salary = salary
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.TextField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    asset = models.IntegerField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    deposit_products = models.ManyToManyField(DepositProducts, blank=True, related_name='userdeposit')
    saving_products = models.ManyToManyField(SavingProducts, blank=True, related_name='usersaving')

    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'