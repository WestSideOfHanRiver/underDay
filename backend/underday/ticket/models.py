from django.db import models

# Create your models here.
class UrMbship(models.Model):
    umem_numb = models.CharField(db_column='UMEM_NUMB', primary_key=True, max_length=10)
    umem_stat = models.CharField(db_column='UMEM_STAT', max_length=8, blank=True, null=True)
    umem_endt = models.CharField(db_column='UMEM_ENDT', max_length=8, blank=True, null=True)
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)
    tmem_numb = models.CharField(db_column='TMEM_NUMB', max_length=8, blank=True, null=True)
    umem_tnum = models.CharField(db_column='UMEM_TNUM', max_length=3, blank=True, null=True)
    umem_unum = models.CharField(db_column='UMEM_UNUM', max_length=3, blank=True, null=True)
    umem_ysno = models.CharField(db_column='UMEM_YSNO', max_length=1, blank=True, null=True)
    umem_inst = models.DateTimeField(db_column='UMEM_INST', blank=True, null=True)
    umem_updt = models.DateTimeField(db_column='UMEM_UPDT', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ur_mbship'