from django.db import models

class TrMbship(models.Model):
    tmem_numb = models.IntegerField(primary_key=True)  # Field name made lowercase.
    user_numb = models.IntegerField()  # Field name made lowercase.
    tmem_name = models.CharField(db_column='TMEM_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmem_expl = models.CharField(db_column='TMEM_EXPL', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tmem_cate = models.CharField(db_column='TMEM_CATE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tmem_grop = models.CharField(db_column='TMEM_GROP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_alr1 = models.CharField(db_column='TMEM_ALR1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_alr2 = models.CharField(db_column='TMEM_ALR2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_maxx = models.CharField(db_column='TMEM_MAXX', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tmem_wait = models.CharField(db_column='TMEM_WAIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_ysno = models.CharField(db_column='TMEM_YSNO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tr_mbship'