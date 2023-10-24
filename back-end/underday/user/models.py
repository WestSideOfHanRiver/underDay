from django.db import models

# Create your models here.
class UrMaster(models.Model):
    user_numb = models.CharField(primary_key=True, max_length=8)  # Field name made lowercase.
    user_idxx = models.CharField(db_column='USER_IDXX', max_length=8, blank=True, null=True)  # Field name made lowercase.
    user_phon = models.CharField(db_column='USER_PHON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_abcd = models.CharField(db_column='USER_ABCD', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_pasw = models.CharField(db_column='USER_PASW', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_pwer = models.IntegerField(db_column='USER_PWER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    user_rptt = models.IntegerField(db_column='USER_RPTT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    user_sumo = models.IntegerField(db_column='USER_SUMO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    user_orig = models.IntegerField(db_column='USER_ORIG', max_length=100, blank=True, null=True)  # Field name made lowercase.
    user_addr = models.IntegerField(db_column='USER_ADDR', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ur_master'