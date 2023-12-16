from django.db import models

class TrMbship(models.Model):
    tmem_numb = models.IntegerField(primary_key=True)  # Field name made lowercase.
    user_numb = models.IntegerField()  # Field name made lowercase.
    tmem_name = models.CharField(db_column='TMEM_NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tmem_expl = models.CharField(db_column='TMEM_EXPL', max_length=300, blank=True, null=True)  # Field name made lowercase.
    tmem_cate = models.CharField(db_column='TMEM_CATE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tmem_grop = models.CharField(db_column='TMEM_GROP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tmem_alr1 = models.CharField(db_column='TMEM_ALR1', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_alr2 = models.CharField(db_column='TMEM_ALR2', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_maxx = models.CharField(db_column='TMEM_MAXX', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tmem_wait = models.CharField(db_column='TMEM_WAIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tmem_ysno = models.CharField(db_column='TMEM_YSNO', max_length=1, blank=True, null=True)  # Field name made lowercase.

#   `TMEM_NUMB` int(8) NOT NULL AUTO_INCREMENT COMMENT '강사수업일련번호', 수업권한권일련번호
#   `USER_NUMB` int(8) DEFAULT NULL COMMENT '강사ID',
#   `TMEM_NAME` varchar(20) DEFAULT NULL COMMENT '강의명',  수업명
#   `TMEM_EXPL` varchar(300) DEFAULT NULL COMMENT '강의실명', 수업장소 -> tmem_spac 
#   `TMEM_CATE` varchar(5) DEFAULT NULL COMMENT '운동구분코드',
#   `TMEM_GROP` char(1) DEFAULT NULL COMMENT '개인/단체구분코드',
#   `TMEM_ALR1` char(2) DEFAULT NULL COMMENT '기본예약확인알림시간',
#   `TMEM_ALR2` char(2) DEFAULT NULL COMMENT '기본수강확정알림시간',
#   `TMEM_MAXX` varchar(3) DEFAULT NULL COMMENT '기본정원',
#   `TMEM_WAIT` char(2) DEFAULT NULL COMMENT '기본대기인원',
#   `TMEM_YSNO` char(1) NOT NULL DEFAULT 'Y' COMMENT '강사수강권사용여부',


    class Meta:
        managed = False
        db_table = 'tr_mbship'