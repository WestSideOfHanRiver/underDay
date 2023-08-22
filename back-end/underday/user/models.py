from django.db import models

# Create your models here.
class UrMaster(models.Model):
    user_numb = models.CharField(db_column='USER_NUMB', primary_key=True, max_length=8)  # Field name made lowercase.
    user_idxx = models.CharField(db_column='USER_IDXX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    user_phon = models.CharField(db_column='USER_PHON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_abcd = models.CharField(db_column='USER_ABCD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_pasw = models.CharField(db_column='USER_PASW', max_length=20, blank=True, null=True)  # Field name made lowercase.

    # user_nick = models.CharField(db_column='USER_NICK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # user_levl = models.CharField(db_column='USER_LEVL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # mast_resp = models.CharField(db_column='MAST_RESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # clas_resp = models.CharField(db_column='CLAS_RESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # memb_resp = models.CharField(db_column='MEMB_RESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # user_orig = models.CharField(db_column='USER_ORIG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # user_imge = models.CharField(db_column='USER_IMGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # user_pref = models.CharField(db_column='USER_PREF', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # user_memo = models.CharField(db_column='USER_MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # user_toke = models.CharField(db_column='USER_TOKE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # user_inst = models.DateTimeField(db_column='USER_INST', blank=True, null=True)  # Field name made lowercase.
    # user_updt = models.DateTimeField(db_column='USER_UPDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ur_master'
        unique_together = (('user_numb', 'user_phon'),)