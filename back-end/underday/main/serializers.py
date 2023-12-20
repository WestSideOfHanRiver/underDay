
from rest_framework import serializers
from .models import UrMaster,TrClass,TrMbship

class UrMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrMaster
        fields = '__all__'

class TrClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrClass
        fields = '__all__'   

class TrMbshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrMbship
        fields = '__all__'  


# SWAGGER_SERIALIZER
class ClassListSerializer(serializers.Serializer):
    clas_numb = serializers.CharField(help_text='수업개설일련번호', required=False)
    clas_name = serializers.CharField(help_text='수업이름', required=False)
    clas_date = serializers.CharField(help_text='수업일자', required=False)
    clas_time = serializers.CharField(help_text='수업시작시간', required=False)
    clas_clos = serializers.CharField(help_text='수업종료시간', required=False)
    tmem_numb = serializers.CharField(help_text='강사수업일련번호', required=False)
    tech_name = serializers.CharField(help_text='강사이름', required=False)
    clas_nmax = serializers.CharField(help_text='정원', required=False)
    clas_cmax = serializers.CharField(help_text='신청인원', required=False)
    clas_wait = serializers.CharField(help_text='총 대기가능 인원', required=False)
    clas_cwai = serializers.CharField(help_text='대기인원', required=False)
    tmem_cate = serializers.CharField(help_text='카테고리', required=False)
    resv_stat = serializers.CharField(help_text='예약시작시간', required=False)
    resv_last = serializers.CharField(help_text='예약마감시간', required=False)
    resv_alr1 = serializers.CharField(help_text='예약확인알림시간', required=False)
    clas_ysno = serializers.CharField(help_text='수업예약마감여부', required=False)
    clas_inst = serializers.CharField(help_text='수업생성일시', required=False)
    clas_updt = serializers.CharField(help_text='업데이트날짜', required=False)
    resv_numb = serializers.CharField(help_text='예약 상태', required=False)
    resv_stat = serializers.CharField(help_text='예약번호', required=False)

class makeClassRequestSerializer(serializers.Serializer):
    clas_numb = serializers.CharField(help_text='수업개설일련번호', required=False)
    tmem_numb = serializers.CharField(help_text='강사수업일련번호', required=False)
    user_numb = serializers.CharField(help_text='유저 아이디', required=False)

class makeClassResponsesSerializer(serializers.Serializer):
    clas_numb = serializers.CharField(help_text='수업개설일련번호', required=False)
    clas_name = serializers.CharField(help_text='수업이름', required=False)
    tmem_numb = serializers.CharField(help_text='강사수업일련번호', required=False)
    user_numb = serializers.CharField(help_text='유저 아이디', required=False)
    clas_date = serializers.CharField(help_text='수업일자', required=False)
    clas_time = serializers.CharField(help_text='수업시작시간', required=False)
    clas_clos = serializers.CharField(help_text='수업종료시간', required=False)
    clas_nmax = serializers.CharField(help_text='정원', required=False)
    clas_cwai = serializers.CharField(help_text='대기인원', required=False)
    resv_stat = serializers.CharField(help_text='예약시작시간', required=False)
    resv_last = serializers.CharField(help_text='예약마감시간', required=False)
    resv_alr1 = serializers.CharField(help_text='예약확인알람시간', required=False)
    
class makeClassPutRequestSerializer(serializers.Serializer):
    clas_numb = serializers.CharField(help_text='수업개설일련번호', required=False)
    tmem_numb = serializers.CharField(help_text='강사수업일련번호', required=False)
    user_numb = serializers.CharField(help_text='유저 아이디', required=False)
    clas_name = serializers.CharField(help_text='수업이름', required=False)
    clas_date = serializers.CharField(help_text='수업일자', required=False)
    clas_time = serializers.CharField(help_text='수업시작시간', required=False)
    clas_clos = serializers.CharField(help_text='수업종료시간', required=False)
    clas_nmax = serializers.CharField(help_text='정원', required=False)
    clas_wait = serializers.CharField(help_text='대기인원', required=False)
    resv_stat = serializers.CharField(help_text='예약시작시간', required=False)
    resv_last = serializers.CharField(help_text='예약마감시간', required=False)
    resv_alr1 = serializers.CharField(help_text='예약확인알람시간', required=False)
    
class ClassRequestSerializer(serializers.Serializer):
    resv_numb = serializers.CharField(help_text='예약일련번호', required=False)
    user_numb = serializers.CharField(help_text='사용자 정보', required=False)
    clas_numb = serializers.CharField(help_text='수강일련번호', required=False)
    tmem_numb = serializers.CharField(help_text='강사수강권번호', required=False)
    resv_stat = serializers.CharField(help_text='예약상태', required=False)

class CallMembersSerializer(serializers.Serializer):
    user_numb = serializers.CharField(help_text='회원번호', required=False)
    user_abcd = serializers.CharField(help_text='A회원B강사C기업', required=False)

class MembersDetailSerializer(serializers.Serializer):
    user_numb = serializers.CharField(help_text='회원번호', required=False)
    user_abcd = serializers.CharField(help_text='A회원B강사C기업', required=False)
