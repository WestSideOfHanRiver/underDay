from django.db import models

# Create your models here.
class UrMaster(models.Model):
    user_numb = models.CharField(db_column='USER_NUMB', primary_key=True, max_length=8)  # Field name made lowercase.
    user_idxx = models.CharField(db_column='USER_IDXX', max_length=8, blank=True, null=True)  # Field name made lowercase.
    user_phon = models.CharField(db_column='USER_PHON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_abcd = models.CharField(db_column='USER_ABCD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_pasw = models.CharField(db_column='USER_PASW', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_pwer = models.CharField(db_column='USER_PWER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_rptt = models.CharField(db_column='USER_RPTT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    user_sumo = models.CharField(db_column='USER_SUMO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_orig = models.CharField(db_column='USER_ORIG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_add1 = models.CharField(db_column='USER_ADD1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_add2 = models.CharField(db_column='USER_ADD2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_add3 = models.CharField(db_column='USER_ADD3', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ur_master'

class UrMbship(models.Model):
    umem_numb = models.CharField(db_column='UMEM_NUMB', primary_key=True, max_length=10)
    umem_stat = models.CharField(db_column='UMEM_STAT', max_length=8, blank=True, null=True)
    umem_endt = models.CharField(db_column='UMEM_ENDT', max_length=8, blank=True, null=True)
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)
    tmem_numb = models.CharField(db_column='TMEM_NUMB', max_length=8, blank=True, null=True)
    umem_tnum = models.CharField(db_column='UMEM_TNUM', max_length=3, blank=True, null=True)
    umem_unum = models.CharField(db_column='UMEM_UNUM', max_length=3, blank=True, null=True)
    umem_ysno = models.CharField(db_column='UMEM_YSNO', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ur_mbship'

class TrMbship(models.Model):
    tmem_numb = models.CharField(db_column='TMEM_NUMB', primary_key=True, max_length=8)
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)
    tmem_name = models.CharField(db_column='TMEM_NAME', max_length=20, blank=True, null=True)
    tmem_expl= models.CharField(db_column='TMEM_EXPL', max_length=300, blank=True, null=True)
    tmem_cate = models.CharField(db_column='TMEM_CATE', max_length=5, blank=True, null=True)
    tmem_grop = models.CharField(db_column='TMEM_GROP', max_length=1, blank=True, null=True)
    tmem_alr1 = models.CharField(db_column='TMEM_ALR1', max_length=2, blank=True, null=True)
    tmem_alr2 = models.CharField(db_column='TMEM_ALR2', max_length=2, blank=True, null=True)
    tmem_maxx = models.CharField(db_column='TMEM_MAXX', max_length=3, blank=True, null=True)
    tmem_wait = models.CharField(db_column='TMEM_WAIT', max_length=2, blank=True, null=True)
    tmem_ysno = models.CharField(db_column='TMEM_YSNO', max_length=1)

    class Meta:
        managed = False
        db_table ='tr_mbship'