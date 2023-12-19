from rest_framework import serializers

# SWAGGER_SERIALIZER
class SelClassSerializer(serializers.Serializer):
    tmem_numb = serializers.CharField(help_text='수업권한권일련번호', required=False)
    user_idxx = serializers.CharField(help_text='강사ID', required=False)
    tmem_name = serializers.CharField(help_text='수업명', required=True)
    tmem_expl = serializers.CharField(help_text='수업장소', required=False)
    tmem_cate = serializers.CharField(help_text='운동구분코드', required=False)
    tmem_grop = serializers.CharField(help_text='개인/단체구분', required=False)
    tmem_alr1 = serializers.CharField(help_text='기본예약확인알림시간', required=False)
    tmem_alr2 = serializers.CharField(help_text='기본수강확정알림시간', required=False)
    tmem_maxx = serializers.CharField(help_text='기본정원', required=False)
    tmem_wait = serializers.CharField(help_text='기본대기인원', required=False)
    tmem_ysno = serializers.CharField(help_text='강사수강권사용여부', required=False)

class NewClassSerializer(serializers.Serializer):
    user_idxx = serializers.CharField(help_text='강사ID', required=True)
    tmem_name = serializers.CharField(help_text='수업명', required=True)
    tmem_expl = serializers.CharField(help_text='수업장소', required=False)
    tmem_cate = serializers.CharField(help_text='운동구분코드', required=False)
    tmem_grop = serializers.CharField(help_text='개인/단체구분', required=False)
    tmem_alr1 = serializers.CharField(help_text='기본예약확인알림시간', required=False)
    tmem_alr2 = serializers.CharField(help_text='기본수강확정알림시간', required=False)
    tmem_maxx = serializers.CharField(help_text='기본정원', required=False)
    tmem_wait = serializers.CharField(help_text='기본대기인원', required=False)

class UpdateClassSerializer(serializers.Serializer):
    tmem_numb = serializers.CharField(help_text='수업권한권일련번호', required=True)
    tmem_name = serializers.CharField(help_text='수업명', required=True)
    tmem_expl = serializers.CharField(help_text='수업장소', required=False)
    tmem_cate = serializers.CharField(help_text='운동구분코드', required=False)
    tmem_grop = serializers.CharField(help_text='개인/단체구분', required=False)
    tmem_alr1 = serializers.CharField(help_text='기본예약확인알림시간', required=False)
    tmem_alr2 = serializers.CharField(help_text='기본수강확정알림시간', required=False)
    tmem_maxx = serializers.CharField(help_text='기본정원', required=False)
    tmem_wait = serializers.CharField(help_text='기본대기인원', required=False)
    tmem_ysno = serializers.CharField(help_text='강사수강권사용여부', required=False)

class DeleteClassSerializer(serializers.Serializer):
    tmem_numb = serializers.CharField(help_text='수업권한권일련번호', required=True)

class SportsListSerializer(serializers.Serializer):
    sports_list = serializers.CharField(help_text='운동리스트', required=True)
    