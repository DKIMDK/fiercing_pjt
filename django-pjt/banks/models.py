
from django.db import models

class DepositProducts(models.Model):
    class Meta:
        app_label = 'banks'
    fin_co_no = models.TextField()
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()

class DepositOptions(models.Model):
    class Meta:
        app_label = 'banks'
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

class SavingProducts(models.Model):
    class Meta:
        app_label = 'banks'
    fin_co_no = models.TextField()
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    join_way = models.TextField()
    spcl_cnd = models.TextField()
    mtrt_int = models.TextField()

class SavingOptions(models.Model):
    class Meta:
        app_label = 'banks'
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()
    rsrv_type_nm = models.TextField(blank=True)

class FilteringOptions(models.Model):
    class Meta:
        app_label = 'banks'
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    fin_prdt_cd = models.TextField()
    save_trm6 = models.FloatField(null=True, blank=True)
    save_trm12 = models.FloatField(null=True, blank=True)
    save_trm24 = models.FloatField(null=True, blank=True)
    save_trm36 = models.FloatField(null=True, blank=True)

class FilteringSavingOptions(models.Model):
    class Meta:
        app_label = 'banks'
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    fin_prdt_cd = models.TextField()
    save_trm6 = models.FloatField(null=True, blank=True)
    save_trm12 = models.FloatField(null=True, blank=True)
    save_trm24 = models.FloatField(null=True, blank=True)
    save_trm36 = models.FloatField(null=True, blank=True)