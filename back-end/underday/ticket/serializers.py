
from rest_framework import serializers
from .models import TrMbship, UrMbship

class TrMbshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrMbship
        fields = '__all__'

class UrMbshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrMbship
        fields = '__all__'


#SWAGGER_SERIALIZER
class TicketListSerializer(serializers.Serializer):
    membership_seq          = serializers.CharField(help_text='회원권일련번호', required=True)
    user_member_seq         = serializers.CharField(help_text='사용자일련번호(회원)', required=True)
    user_member_id          = serializers.CharField(help_text='사용자ID(회원)', required=True)
    user_member_nm          = serializers.CharField(help_text='사용자명(회원)', required=True)
    class_seq               = serializers.CharField(help_text='강사수업일련번호', required=True)
    class_nm                = serializers.CharField(help_text='강의명', required=True)
    membership_stat_date    = serializers.CharField(help_text='회원권이용시작일자', required=True)
    membership_end_date     = serializers.CharField(help_text='회원권이용종료일자', required=True)
    membership_join_number  = serializers.CharField(help_text='회원권등록회차', required=True)
    membership_use_number   = serializers.CharField(help_text='회원권사용회차', required=True)
    membership_use_yn       = serializers.CharField(help_text='회원권사용가능여부', required=True)
    user_teach_seq          = serializers.CharField(help_text='사용자일련번호(강사)', required=True)
    user_teach_id           = serializers.CharField(help_text='사용자ID(강사)', required=True)
    user_teach_nm           = serializers.CharField(help_text='사용자명(강사)', required=True)

class TicketCreateSerializer(serializers.Serializer):
    tmem_numb = serializers.CharField(help_text='강사수업일련번호', required=True)
    user_idxx = serializers.CharField(help_text='회원ID', required=True)
    umem_stat = serializers.CharField(help_text='회원권이용시작일자', required=True)
    umem_endt = serializers.CharField(help_text='회원권이용종료일자', required=True)
    umem_tnum = serializers.CharField(help_text='회원권등록회차', required=False)

class TicketUpdateSerializer(serializers.Serializer):
    umem_numb = serializers.CharField(help_text='회원권일련번호', required=True)
    umem_stat = serializers.CharField(help_text='회원권이용시작일자', required=True)
    umem_endt = serializers.CharField(help_text='회원권이용종료일자', required=True)
    umem_tnum = serializers.CharField(help_text='회원권등록회차', required=False)
    umem_unum = serializers.CharField(help_text='회원권사용회차', required=False)
    umem_ysno = serializers.CharField(help_text='회원권사용가능여부', required=False)
