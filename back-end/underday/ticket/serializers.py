
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
    user_numb = serializers.CharField(help_text='사용자 일련번호', required=True)

class TicketCreateSerializer(serializers.Serializer):
    tmem_numb = serializers.CharField(help_text='강사수업일련번호', required=True)
    user_idxx = serializers.CharField(help_text='회원ID', required=True)
    umem_stat = serializers.CharField(help_text='회원권이용시작일자', required=True)
    umem_endt = serializers.CharField(help_text='회원권이용종료일자', required=True)
    umem_tnum = serializers.CharField(help_text='회원권등록회차', required=False)

class TicketUpdateSerializer(serializers.Serializer):
    umem_numb = serializers.CharField(help_text='사용자 일련번호', required=True)
    umem_stat = serializers.CharField(help_text='회원권이용시작일자', required=True)
    umem_endt = serializers.CharField(help_text='회원권이용종료일자', required=True)
    umem_tnum = serializers.CharField(help_text='회원권등록회차', required=False)
    umem_unum = serializers.CharField(help_text='회원권사용회차', required=False)
    umem_ysno = serializers.CharField(help_text='회원권사용가능여부', required=False)

class trMbshipListSerializer(serializers.Serializer):
    umem_numb = serializers.CharField(help_text='사용자 일련번호', required=True)