from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    # database에서 조회된 user의 정보가 user로 들어오게 된다. (요청한 user의 정보)
    def get_token(cls, user):
		# 가지고 온 user의 정보를 바탕으로 token을 생성한다.
        token = super().get_token(user)

        # 로그인한 사용자의 클레임 설정하기.
        token['user_numb'] = user.user_numb
        token['user_idxx'] = user.user_idxx
        token['user_name'] = user.user_name
        token['user_abcd'] = user.user_abcd

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer