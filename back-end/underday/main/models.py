from django.db import models

class UrMbship(models.Model):
    umem_numb = models.CharField(db_column='UMEM_NUMB', primary_key=True, max_length=10)
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)
    tmem_numb = models.CharField(db_column='TMEM_NUMB', max_length=8, blank=True, null=True)
    umem_stat = models.CharField(db_column='UMEM_STAT', max_length=8, blank=True, null=True)
    # umem_endt = models.CharField(db_column='UMEM_ENDT', max_length=8, blank=True, null=True)
    umem_tnum = models.CharField(db_column='UMEM_TNUM', max_length=3, blank=True, null=True)
    umem_unum = models.CharField(db_column='UMEM_UNUM', max_length=3, blank=True, null=True)
    umem_ysno = models.CharField(db_column='UMEM_YSNO', max_length=1, blank=True, null=True)
    umem_inst = models.DateTimeField(db_column='UMEM_INST', blank=True, null=True)
    umem_updt = models.DateTimeField(db_column='UMEM_UPDT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ur_mbship'


class TrClass(models.Model):
    clas_numb = models.CharField(db_column='CLAS_NUMB', primary_key=True, max_length=7)
    clas_date = models.CharField(db_column='CLAS_DATE', max_length=8)
    clas_time = models.CharField(db_column='CLAS_TIME', max_length=4)
    clas_clos = models.CharField(db_column='CLAS_CLOS', max_length=4)
    tmem_numb = models.CharField(db_column='TMEM_NUMB', max_length=8, blank=True, null=True)
    clas_nmax = models.CharField(db_column='CLAS_NMAX', max_length=2, blank=True, null=True)
    clas_wait = models.CharField(db_column='CLAS_WAIT', max_length=2, blank=True, null=True)
    resv_stat = models.CharField(db_column='RESV_STAT', max_length=8, blank=True, null=True)
    resv_last = models.CharField(db_column='RESV_LAST', max_length=8, blank=True, null=True)
    resv_alr1 = models.CharField(db_column='RESV_ALR1', max_length=2, blank=True, null=True)
    clas_ysno = models.CharField(db_column='CLAS_YSNO', max_length=1, blank=True, null=True)
    clas_inst = models.DateTimeField(db_column='CLAS_INST', blank=True, null=True)
    clas_updt = models.DateTimeField(db_column='CLAS_UPDT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tr_class'
        unique_together = (('clas_numb', 'clas_date', 'clas_time'),)


class TrMbship(models.Model):
    tmem_numb = models.CharField(db_column='TMEM_NUMB', primary_key=True, max_length=8)
    user_numb = models.CharField(db_column='USER_NUMB', max_length=8, blank=True, null=True)
    tmem_name = models.CharField(db_column='TMEM_NAME', max_length=20, blank=True, null=True)
    tmem_expl= models.CharField(db_column='TMEM_EXPL', max_length=300, blank=True, null=True)
    tmem_cate = models.CharField(db_column='TMEM_CATE', max_length=5, blank=True, null=True)
    tmem_grop = models.CharField(db_column='TMEM_GROP', max_length=1, blank=True, null=True)
    # tmem_duet = models.CharField(db_column='TMEM_DUET', max_length=2, blank=True, null=True)
    tmem_maxx = models.CharField(db_column='TMEM_MAXX', max_length=3, blank=True, null=True)
    tmem_alr1 = models.CharField(db_column='TMEM_ALR1', max_length=2, blank=True, null=True)
    tmem_alr2 = models.CharField(db_column='TMEM_ALR2', max_length=2, blank=True, null=True)
    tmem_wait = models.CharField(db_column='TMEM_WAIT', max_length=2, blank=True, null=True)
    tmem_ysno = models.CharField(db_column='TMEM_YSNO', max_length=1)
    tmem_inst = models.DateTimeField(db_column='TMEM_INST', blank=True, null=True)
    tmem_updt = models.DateTimeField(db_column='TMEM_UPDT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tr_mbship'


class UrMaster(models.Model):
    user_numb = models.CharField(db_column='USER_NUMB', primary_key=True, max_length=8)
    user_name = models.CharField(db_column='USER_NAME', max_length=20, blank=True, null=True)
    user_phon = models.CharField(db_column='USER_PHON', max_length=20)
    user_nick = models.CharField(db_column='USER_NICK', max_length=20, blank=True, null=True)
    user_pasw = models.CharField(db_column='USER_PASW', max_length=25, blank=True, null=True)
    user_abcd = models.CharField(db_column='USER_ABCD', max_length=3, blank=True, null=True)
    user_orig = models.CharField(db_column='USER_ORIG', max_length=40, blank=True, null=True)
    user_imge = models.CharField(db_column='USER_IMGE', max_length=200, blank=True, null=True)
    user_exep = models.CharField(db_column='USER_EXEP', max_length=300, blank=True, null=True)
    user_pref = models.CharField(db_column='USER_PREF', max_length=100, blank=True, null=True)
    user_addr = models.CharField(db_column='USER_ADDR', max_length=100, blank=True, null=True)
    user_inst = models.DateTimeField(db_column='USER_INST', blank=True, null=True)
    user_updt = models.DateTimeField(db_column='USER_UPDT', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ur_master'
        unique_together = (('user_numb', 'user_phon'),)


class ReMaster(models.Model):
    resv_numb = models.CharField(db_column='RESV_NUMB', primary_key=True, max_length=7)
    clas_numb = models.CharField(db_column='CLAS_NUMB', max_length=7, blank=True, null=True)
    clas_date = models.CharField(db_column='CLAS_DATE', max_length=8, blank=True, null=True)
    clas_time = models.CharField(db_column='CLAS_TIME', max_length=4, blank=True, null=True)
    umem_numb = models.CharField(db_column='UMEM_NUMB', max_length=10, blank=True, null=True)
    resv_code = models.CharField(db_column='RESV_CODE', max_length=4, blank=True, null=True)
    resv_memo = models.CharField(db_column='RESV_MEMO', max_length=200, blank=True, null=True)
    stat_date = models.CharField(db_column='STAT_DATE', max_length=8, blank=True, null=True)
    canc_date = models.CharField(db_column='CANC_DATE', max_length=8, blank=True, null=True)
    canc_ysno = models.CharField(db_column='CANC_YSNO', max_length=1, blank=True, null=True)
    canc_name = models.CharField(db_column='CANC_NAME', max_length=10, blank=True, null=True)
    canc_reas = models.CharField(db_column='CANC_REAS', max_length=200, blank=True, null=True)
    resv_inst = models.DateTimeField(db_column='RESV_INST', blank=True, null=True)
    resv_updt = models.DateTimeField(db_column='RESV_UPDT', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 're_master'
