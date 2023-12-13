
from rest_framework import serializers


# SWAGGER_SERIALIZER
class UserSignupSerializer(serializers.Serializer):
    user_idxx = serializers.CharField(help_text='사용자ID', required=True)
    password1 = serializers.CharField(help_text='비밀번호1', required=True)
    password2 = serializers.CharField(help_text='비밀번호2', required=True)
    user_phon = serializers.CharField(help_text='휴대폰번호', required=True)
    user_name = serializers.CharField(help_text='사용자명', required=False)
    user_abcd = serializers.CharField(help_text='사용자구분(A:회원, B:강사, C:기업)', required=True)
    user_orig = serializers.CharField(help_text='소속명', required=False)
    user_conb = serializers.CharField(help_text='사업자등록번호', required=False)
    user_add1 = serializers.CharField(help_text='우편번호', required=False)
    user_add2 = serializers.CharField(help_text='주소', required=False)

class UserChkSerializer(serializers.Serializer):
    user_idxx = serializers.CharField(help_text='사용자ID', required=True)

class UserLoginSerializer(serializers.Serializer):
    user_idxx = serializers.CharField(help_text='사용자ID', required=True)
    password = serializers.CharField(help_text='비밀번호', required=True)