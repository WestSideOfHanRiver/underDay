from django.db import models

class ReMaster(models.Model):
    resv_numb = models.CharField(db_column='RESV_NUMB', primary_key=True, max_length=8)  # Field name made lowercase.
    clas_numb = models.CharField(db_column='CLAS_NUMB', max_length=6, blank=True, null=True)  # Field name made lowercase.
    clas_date = models.CharField(db_column='CLAS_DATE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    clas_time = models.CharField(db_column='CLAS_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    umem_numb = models.CharField(db_column='UMEM_NUMB', max_length=10, blank=True, null=True)  # Field name made lowercase.
    resv_code = models.CharField(db_column='RESV_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    resv_memo = models.CharField(db_column='RESV_MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    stat_date = models.CharField(db_column='STAT_DATE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    canc_ysno = models.CharField(db_column='CANC_YSNO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    canc_id = models.CharField(db_column='CANC_ID', max_length=8, blank=True, null=True)  # Field name made lowercase.
    canc_reason = models.CharField(db_column='CANC_REASON', max_length=200, blank=True, null=True)  # Field name made lowercase.
    canc_date = models.CharField(db_column='CANC_DATE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    resv_updt = models.DateTimeField(db_column='RESV_UPDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 're_master'


class TrClass(models.Model):
    clas_numb = models.CharField(db_column='CLAS_NUMB', primary_key=True, max_length=6)  # Field name made lowercase.
    clas_date = models.CharField(db_column='CLAS_DATE', max_length=8)  # Field name made lowercase.
    clas_time = models.CharField(db_column='CLAS_TIME', max_length=4)  # Field name made lowercase.
    tmem_numb = models.CharField(db_column='TMEM_NUMB', max_length=8, blank=True, null=True)  # Field name made lowercase.
    clas_nmax = models.CharField(db_column='CLAS_NMAX', max_length=3, blank=True, null=True)  # Field name made lowercase.
    clas_wait = models.CharField(db_column='CLAS_WAIT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    clas_last = models.CharField(db_column='CLAS_LAST', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clas_alr1 = models.CharField(db_column='CLAS_ALR1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clas_alr2 = models.CharField(db_column='CLAS_ALR2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    clas_ysno = models.CharField(db_column='CLAS_YSNO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clas_inst = models.DateTimeField(db_column='CLAS_INST', blank=True, null=True)  # Field name made lowercase.
    clas_updt = models.DateTimeField(db_column='CLAS_UPDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tr_class'
        unique_together = (('clas_numb', 'clas_date', 'clas_time'),)


class TrMbship(models.Model):
    tmem_numb = models.CharField(db_column='TMEM_NUMB', primary_key=True, max_length=10)  # Field name made lowercase.
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tmem_name = models.CharField(db_column='TMEM_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmem_cate = models.CharField(db_column='TMEM_CATE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    tmem_grop = models.CharField(db_column='TMEM_GROP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmem_duet = models.CharField(db_column='TMEM_DUET', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_alr1 = models.CharField(db_column='TMEM_ALR1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_alr2 = models.CharField(db_column='TMEM_ALR2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_wait = models.CharField(db_column='TMEM_WAIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_ysno = models.CharField(db_column='TMEM_YSNO', max_length=2)  # Field name made lowercase.
    tmem_inst = models.DateTimeField(db_column='TMEM_INST', blank=True, null=True)  # Field name made lowercase.
    tmem_updt = models.DateTimeField(db_column='TMEM_UPDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tr_mbship'


class UrMaster(models.Model):
    user_numb = models.CharField(db_column='USER_NUMB', primary_key=True, max_length=8)  # Field name made lowercase.
    user_phon = models.CharField(db_column='USER_PHON', max_length=20)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_nick = models.CharField(db_column='USER_NICK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_abcd = models.CharField(db_column='USER_ABCD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_levl = models.CharField(db_column='USER_LEVL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mast_resp = models.CharField(db_column='MAST_RESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clas_resp = models.CharField(db_column='CLAS_RESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    memb_resp = models.CharField(db_column='MEMB_RESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_orig = models.CharField(db_column='USER_ORIG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_imge = models.CharField(db_column='USER_IMGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_pref = models.CharField(db_column='USER_PREF', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_memo = models.CharField(db_column='USER_MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    user_toke = models.CharField(db_column='USER_TOKE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_pasw = models.CharField(db_column='USER_PASW', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_inst = models.DateTimeField(db_column='USER_INST', blank=True, null=True)  # Field name made lowercase.
    user_updt = models.DateTimeField(db_column='USER_UPDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ur_master'
        unique_together = (('user_numb', 'user_phon'),)


class UrMbship(models.Model):
    umem_numb = models.CharField(db_column='UMEM_NUMB', primary_key=True, max_length=10)  # Field name made lowercase.
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tmem_numb = models.CharField(db_column='TMEM_NUMB', max_length=8, blank=True, null=True)  # Field name made lowercase.
    umem_stat = models.CharField(db_column='UMEM_STAT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    umem_endt = models.CharField(db_column='UMEM_ENDT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    umem_tnum = models.CharField(db_column='UMEM_TNUM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    umem_unum = models.CharField(db_column='UMEM_UNUM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    umem_pyno = models.CharField(db_column='UMEM_PYNO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    umem_inst = models.DateTimeField(db_column='UMEM_INST', blank=True, null=True)  # Field name made lowercase.
    umem_updt = models.DateTimeField(db_column='UMEM_UPDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ur_mbship'
