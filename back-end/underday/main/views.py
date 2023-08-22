from django.shortcuts import render, redirect
from .models import UrMaster
from .serializers import UrMasterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
@api_view(['GET'])
def user_list(request):
    users = UrMaster.objects.all()
    serializer = UrMasterSerializer(users,many=True)
    return Response(serializer.data)

# 메인페이지 요구사항 
# 월/일 에 해당하는 모든 예약데이터, 수강가능한 일정
# GET 요청시 유저ID와 날짜를 받아서 필터 
