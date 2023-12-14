from django.urls import path
from . import views
# from user.jwt_claim_serializer import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenVerifyView,
#     TokenRefreshView,
# )

urlpatterns = [
    # 로그인/회원가입
    path("signup/", views.UserSignupAPI.as_view(), name="signup"),
    path("login/", views.UserLoginAPI.as_view(), name="login"),
    path("chkUserId/", views.ChkUserAPI.as_view(), name="chkUserId"),

    # 마이페이지
    path("mypageSel/", views.MypageSelAPI.as_view(), name="mypageSel"),
    path("mypageUpdate/", views.MypageUpdateAPI.as_view(), name="mypageUpdate"),
    
    # 토큰
    # TokenObtainPairView : 토큰을 생성해주는 뷰
    # TokenVerifyView : 토큰 유효성 확인 뷰
    # TokenRefreshView : refresh 토큰으로 access 토큰을 재밸급하는 뷰
    # path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
	# path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

