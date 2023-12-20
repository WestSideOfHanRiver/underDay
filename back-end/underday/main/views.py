from django.shortcuts import render, redirect
from .models import UrMaster,UrMbship, TrMbship, TrClass, ReMaster
from .serializers import UrMasterSerializer,TrClassSerializer,TrMbshipSerializer,ClassListSerializer,MembersDetailSerializer,CallMembersSerializer,ClassRequestSerializer,makeClassRequestSerializer,makeClassResponsesSerializer,makeClassPutRequestSerializer
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# @csrf_exempt
# @api_view(['GET'])
# def user_list(request):
class UserListAPI(APIView):
    @swagger_auto_schema(tags=['user_list'], responses={201:UrMasterSerializer})
    def get(self, request):
        users = UrMaster.objects.all()
        serializer = UrMasterSerializer(users,many=True)
        return Response(serializer.data)


# 제목 : 캘린더 메인페이지  
# 로직 : 월/일 에 해당하는 모든 데이터, 수강가능한 일정
# 요청 : id, date, time
# 리턴 : 수강가능 강의 리스트
# id, date20230303, time1430
# ur_master -> ur_mbship -> tr_class
######################    Serializer 사용한 class_list 함수   ###########################
# API : http://127.0.0.1:8000/classlist/
# @csrf_exempt
# @api_view(['GET'])
# def class_list(request):
class ClassListAPI(APIView):
    @swagger_auto_schema(tags=['캘린더 메인페이지'], responses={201:ClassListSerializer})
    def get(self, request):

        usernumb = request.GET.get('user_numb', None)
        date = request.GET.get('date', None)
        userabcd = request.GET.get('user_abcd', None)
        # 현재시간 이후에 보이는건 나중에 시간 데이터 추가
        if userabcd == 'A':
            cursor = connection.cursor()
            strSql = '''SELECT B.clas_numb, B.clas_name, B.clas_date, B.clas_time, B.clas_clos,A.tmem_numb,D.user_name AS tech_name,
                    B.clas_nmax,B.clas_cmax,B.clas_wait,B.clas_cwai,C.tmem_cate,B.resv_stat,B.resv_last,B.resv_alr1,B.clas_ysno,B.clas_inst, B.clas_updt,E.resv_numb,E.resv_stat
                    FROM ur_mbship AS A LEFT JOIN tr_class AS B ON A.TMEM_NUMB = B.TMEM_NUMB LEFT JOIN tr_mbship AS C ON A.TMEM_NUMB = C.TMEM_NUMB 
                    LEFT JOIN ur_master AS D ON C.USER_NUMB = D.USER_NUMB LEFT JOIN re_master AS E ON A.UMEM_NUMB = E.UMEM_NUMB AND B.CLAS_NUMB = E.CLAS_NUMB
                    WHERE A.USER_NUMB = (%s) AND A.UMEM_YSNO = 'Y' AND B.clas_date = (%s) ORDER BY CLAS_TIME '''
            params = [usernumb,date]
            with connection.cursor() as cursor:
                cursor.execute(strSql, params)
                queryset = dictfetchall(cursor)
            return Response(queryset)
        
        if userabcd == 'B': # 강사일때
            cursor = connection.cursor()
            strSql = '''SELECT B.clas_numb, B.clas_name, B.clas_date, B.clas_time, B.clas_clos,A.tmem_numb,C.user_name AS tech_name,
                B.clas_nmax,B.clas_cmax,B.clas_wait,B.clas_cwai,A.tmem_cate,B.resv_stat,B.resv_last,B.resv_alr1,B.clas_ysno,B.clas_inst, B.clas_updt
                FROM tr_mbship AS A LEFT JOIN tr_class AS B ON A.TMEM_NUMB = B.TMEM_NUMB 
                LEFT JOIN ur_master AS C ON A.USER_NUMB = C.USER_NUMB 
                WHERE A.USER_NUMB = (%s) AND B.clas_date = (%s) ORDER BY CLAS_TIME'''
            params = [usernumb,date]
            with connection.cursor() as cursor:
                cursor.execute(strSql, params)
                queryset = dictfetchall(cursor)
            return Response(queryset)


    



######################################################################################

# 제목 : 당월 예약 가능 일자 표시
# 요청 : 날짜, 요청자id
# 리턴 : ok,error
# API : http://127.0.0.1:8000/getclassdate/
# user_numb, date
# @csrf_exempt
# @api_view(['GET'])
# def get_classdate(request):
class GetClassdateAPI(APIView):
    @swagger_auto_schema(tags=['예약'], operation_id='당월 예약 가능 일자 조회 API', operation_description='당월 예약 가능 일자', responses={200:TrClassSerializer})
    def get(self, request):
        data = request.data
        resvnumb = data["user_numb"] # (선택)예약일련번호 예약 취소 할경우!
        date = data["date"] # 사용자 정보
        user_abcd = data["user_abcd"]
        if user_abcd == 'A': # 회원일때

            clas_queryset = TrClass.objects.filter(clas_date__startswith=date[:4])
            print(clas_queryset)
            return HttpResponse(status=200) 
######################################################################################

# 제목 : 예약버튼 이벤트
# 로직 : 예약하기, 예약 취소하기
# 요청 : 수강번호, 요청자id
# 리턴 : ok,error
# API : http://127.0.0.1:8000/classrequest/
# 
# 예약일련번호 resv_numb, 수업개설일련번호 CLAS_NUMB,수업날짜 CLAS_DATE, 회원권 일련번호 UMEM_NUMB , reserve_status 현재 예약 상태

# @csrf_exempt
# @api_view(['PUT'])
# def class_request(request):
class ClassRequestAPI(APIView):
    @swagger_auto_schema(tags=['예약'], operation_id='예약버튼 API', operation_description='예약버튼', responses={201:ClassRequestSerializer})
    def put(self, request):
        data = request.data
        resvnumb = data["resv_numb"] # (선택)예약일련번호 예약 취소 할경우!
        usernumb = data['user_numb'] # 사용자 정보
        clasnumb = data['clas_numb'] # 수강일련번호
        tmemnumb = data['tmem_numb'] # 강사수강권번호
        resvstat = data['resv_stat'] # 예약상태

        if resvstat =='00' : # 예약가능,대기가능 상태일때 예약 신청

            # 1. 예약 정원, 대기자 확인
            # 신청가능(00) - 신청가능 정원에 여유있음
            # 예약완료(01) - 신청완료 정원안에 들어감-> 예약 취소(상태00업데이트) 가능 
            # 예약대기(02) - 신청완료 정원 초과, 대기자에 들어감 - >예약취소 가능 취소로직에서 대기자 예약테이블 업데이트
            # 예약확정(03) - 예약 후 기간지남, 예약 후 강사가 마감처리함
            # 예약반려(04) - 강사가 반려처리함
            # 예약마감(05) - 기간지남
            trcl_ob = TrClass.objects.filter(clas_numb=clasnumb)
            if not trcl_ob.exists():  # 결과가 존재하는지 확인 -> 결과가 없으면
                return HttpResponse(status=400, content=f"예약 가능한 강의가 없습니다")
            else:
                trcl_instance = trcl_ob[0]
                print(trcl_instance)
                cmax = int(trcl_instance.clas_cmax)
                nmax = int(trcl_instance.clas_nmax)
                wait = int(trcl_instance.clas_wait)
                cwai = int(trcl_instance.clas_cwai)
                # 현정원이 여유가 있으면
                if cmax < nmax or  cwai < wait:
                    # 2. 내 수강권 중 가장 오래된 내역 불러와서 사용 횟수 확인
                    mbsh_ob = UrMbship.objects.filter(user_numb=usernumb, tmem_numb=tmemnumb, umem_ysno= 'Y').order_by('umem_numb')# 유저 맴버쉽 가져오기
                    if mbsh_ob.exists():  # 결과가 존재하는지 확인
                        mbsh_instance = mbsh_ob[0]  # 첫 번째 객체를 얻음
                    else:
                        return HttpResponse(status=400, content=f"활성화된 수강권이 없습니다")

                    total_numb = int(mbsh_instance.umem_tnum)
                    use_numb = int(mbsh_instance.umem_unum)

                    if use_numb < total_numb:
                        use_numb += 1
                        mbsh_instance.umem_unum = str(use_numb)
                        # 1의 현정원, 현대기자 업데이트
                        if cmax < nmax :
                            trcl_instance.clas_cmax = cmax + 1
                            try:
                                trcl_instance.save()
                                resvstat = '01' # 정원내 예약완료
                            except:
                                return HttpResponse(status=400, content=f"현재 정원 저장 실패")
                        elif cwai < wait:
                            trcl_instance.clas_cwai = cwai + 1
                            try:
                                trcl_instance.save()
                                resvstat = '02' # 예약대기      
                            except:
                                return HttpResponse(status=400, content=f"현재 대기인원 저장 실패")
                        # 만약 카운트가 다 찼다면 멤버쉽 비활성화
                        if use_numb == total_numb:
                            mbsh_instance.umem_ysno = 'N'
                        try:
                            mbsh_instance.save()
                        except:
                            return HttpResponse(status=400, content=f"멤버쉽 횟수 증가 혹은 멤버쉽 상태 변경 저장 실패")

                        resved_ob = ReMaster.objects.filter(clas_numb = clasnumb, resv_idxx=usernumb,resv_stat='00').order_by('resv_numb').first()
                        if resved_ob :
                            resved_ob.resv_stat = resvstat
                            try:
                                resved_ob.save()
                                return HttpResponse(status=200)
                            except Exception as e:
                                # 저장에 실패한 경우 
                                print(f"Error during save: {e}")
                                # 저장에 실패한 경우 
                                return HttpResponse(status=400, content=f"기존 예약데이터 저장 실패")
                        else:
                            # 대기신청(상태값없음 프론트에서 처리) - 대기자 정원 여유 있음
                            # resv_numb_v 자동생성
                            relast = ReMaster.objects.order_by('-resv_numb').first()
                            re_lastnumb = int(relast.resv_numb) + 1
                    
                            clasnumb_v = trcl_instance.clas_numb  # 수업일련번호
                            resvidxx_v = usernumb # 신청자
                            clasdate_v = trcl_instance.clas_date # 수업일자
                            clastime_v = trcl_instance.clas_time # 수업상세시간
                            umemnumb_v = mbsh_ob[0].umem_numb # 정원 2자리
                            resvstat_v = resvstat # 예약상태 신청가능(00), 예약완료(01), 예약대기(02), 예약확정(03), 예약반려(04), 예약마감(05)
                            cancysno_v = 'N'

                            # 모델 객체 생성 및 저장
                            new_data = ReMaster(resv_numb = re_lastnumb, resv_idxx = resvidxx_v, clas_numb=clasnumb_v, clas_date=clasdate_v,clas_time=clastime_v,umem_numb=umemnumb_v,
                                                resv_stat=resvstat_v,canc_ysno=cancysno_v)
                            try:
                                new_data.save()  # 데이터 저장 시도
                                return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
                            except Exception as e:
                                # 저장에 실패한 경우 
                                print(f"Error during save: {e}")
                                # 저장에 실패한 경우 
                                return HttpResponse(status=400, content=f"예약데이터 저장 실패1")
                    else:
                        return HttpResponse(status=400, content=f"예약데이터 저장 실패1")
    ############################ 예약 취소 ##################################
        # 예약 번호가 있거나 예약 완료 혹은 예약 대기인 경우, 예약 취소 가능
        if resvnumb and  (resvstat =='01' or resvstat =='02' ):
            

            trcl_ob = TrClass.objects.filter(clas_numb=clasnumb)
            if not trcl_ob.exists():  # 결과가 존재하는지 확인 -> 결과가 없으면
                return HttpResponse(status=400, content=f"취소 가능한 강의가 없습니다")
            else:
                trcl_instance = trcl_ob[0]
                cmax = int(trcl_instance.clas_cmax)
                wait = int(trcl_instance.clas_wait)
                if resvstat =='01': # 내가 예약완료였던 경우
                    # 대기자 선출선납, 예약대기가 있으면
                    wait_ob =  ReMaster.objects.filter(clas_numb=clasnumb,resv_stat='02').order_by('resv_numb').first()  # 대기자  
                    resv_ob =  ReMaster.objects.filter(clas_numb=clasnumb,resv_idxx=usernumb,resv_stat='01').order_by('resv_numb').first()  # 예약자
                    clas_ob =  TrClass.objects.filter(clas_numb=clasnumb).first() 
                    if resv_ob and clas_ob:
                        # 대기자 있으면 대기인원CWAI 줄고, CMAX 그대로
                        if wait_ob:
                            print(wait_ob)
                            wait_ob.resv_stat= '01'
                            cwai_waitnumb = int(clas_ob.clas_cwai) - 1
                            clas_ob.clas_cwai = cwai_waitnumb
                        # 대기자 없으면 CMAX 감소
                        else:
                            cmax_waitnumb = int(clas_ob.clas_cmax) - 1
                            clas_ob.clas_cmax = cmax_waitnumb
                        resv_ob.resv_stat= '00'

                        try:
                            if resv_ob:
                                resv_ob.save()
                            if wait_ob:
                                wait_ob.save() 
                            if clas_ob:
                                clas_ob.save()
                        except Exception as e:
                            print(f"Error during save: {e}")
                            return HttpResponse(status=400, content=f"대기자 상태 변경 실패1")
                    else:
                        return HttpResponse(status=400, content=f"예약내역이나, 강의정보를 불러올 수 없습니다")

                # 내가 예약 대기자였던 경우의 취소프로세스
                elif resvstat =='02': # 내가 예약대기였던 경우
                    resv_ob =  ReMaster.objects.filter(clas_numb=clasnumb,resv_idxx=usernumb,resv_stat='02').order_by('resv_numb').first()  
                    clas_ob =  TrClass.objects.filter(clas_numb=clasnumb).first() 
                    resv_ob.resv_stat= '00'
                    waitnumb = int(clas_ob.clas_cwai) - 1
                    clas_ob.clas_cwai = waitnumb
                    try:
                        resv_ob.save()
                        clas_ob.save()
                    except Exception as e:
                        print(f"Error during save: {e}")
                        return HttpResponse(status=400, content=f"대기자 상태 변경 실패2")

            queryset = ReMaster.objects.get(resv_numb = resvnumb)   
            if queryset:
                urmb_ob =  UrMbship.objects.filter(umem_numb=queryset.umem_numb).order_by('umem_numb').first()


                unum = int(urmb_ob.umem_unum)
                # 회원권 사용횟수 증가
                urmb_ob.umem_unum = unum - 1

                try:
                    urmb_ob.save()
                    return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
                except Exception as e:
                    # 저장에 실패한 경우 
                    print(f"Error during save: {e}")
                    # 저장에 실패한 경우 
                    return HttpResponse(status=400, content=f"예약취소, 회원권 횟수 차감 실패")

                # 예약테이블 상태 변경
                queryset.resv_stat = resvstat


        
            # 추후 이미 신청중인 경우도 표시해야함
           




# API : http://127.0.0.1:8000/trmbship/
# 제목 : 강의생성 수강 가능 리스트 리턴
# 로직 : 너 수강권 뭐있음?
# 요청 : ID : 00000000
# 리턴 : 수강권 리스트
# @csrf_exempt
# @api_view(['GET'])
# def trmbship_list(request):
class TrmbshipListAPI(APIView):
    @swagger_auto_schema(tags=['Class'], operation_id='강의생성 수강 가능 리스트 조회 API', operation_description='강의생성 수강 가능 리스트', responses={201:TrMbshipSerializer})
    def get(self, request):
        data = request.data
        usernumb = data['user_numb']

        trmb_ob = TrMbship.objects.filter(user_numb=usernumb) # 강의 정보 가져오기
        serializer = TrMbshipSerializer(trmb_ob,many=True)
        return Response(serializer.data)

# API : http://127.0.0.1:8000/make_class/
# 제목 : 강의생성 기본값 셋팅로직
# 로직 : 강의 생성 버튼 눌렀을때 기본값 셋팅
# 요청 : 강의명, 강의시작시간, 종료시간, 날짜, 예약마감, 개인단체구분, 정원, 운동구분 코드, 센터명
# 리턴 : x
# @csrf_exempt
# @api_view(['POST','PUT','DELETE'])
# def make_class(request):
class MakeClassAPI(APIView):
    @swagger_auto_schema(tags=['Class'], operation_id='강의생성 API', operation_description='강의생성', request_body=makeClassRequestSerializer, responses={201:makeClassResponsesSerializer})
    def post(self, request):
        clasnumb = request.data["clas_numb"] # 삭제 수정에는 필요, 등록일땐 빈칸
        tmemnumb = request.data["tmem_numb"] # 수강권번호
        user_numb = request.data["user_numb"] # ID값

        last_serial = TrClass.objects.order_by('-clas_numb').first()
        if last_serial:
            last_date = last_serial.clas_numb[:6]

            if last_date == datetime.now().strftime('%y%m%d'):
                sum_serial = int(last_serial.clas_numb[6:]) + 1
                formatted_num = f"{sum_serial:04d}"
                new_serial = str(datetime.now().strftime('%y%m%d')) + formatted_num
            else:
                new_serial = str(datetime.now().strftime('%y%m%d')) + '0000'

        
        clasdate_v = request.data["clas_date"] # 강의시작시간 
        clastime_v = request.data["clas_time"] # 수업시작시간 4자리 1130
        clasname_v = request.data["clas_name"] # 강의이름
        clasclos_v = request.data["clas_clos"] # 수업종료시간 4자리 1130
        clasnmax_v = request.data["clas_nmax"] # 정원 2자리
        claswait_v = request.data["clas_wait"] # 대기인원 2자리
        clascmax_v = 0 # 현 정원 2자리
        clascwai_v = 0 # 현 대기인원 2자리
        resvstat_v = request.data["resv_stat"] # 예약시작시간 12자리 202302011130
        resvlast_v = request.data["resv_last"] # 예약마감시간 12자리 202302211200
        resvalr1_v = request.data["resv_alr1"] # 예약마감전 알람시간 2자리 11시간
 
        # 모델 객체 생성 및 저장
        new_data = TrClass(clas_numb=new_serial, clas_date=clasdate_v,clas_time=clastime_v,clas_nmax=clasnmax_v,clas_name=clasname_v,
                            clas_wait=claswait_v,resv_stat=resvstat_v,resv_last=resvlast_v,resv_alr1=resvalr1_v, clas_cwai=clascwai_v,
                            clas_cmax=clascmax_v, clas_clos=clasclos_v, tmem_numb=tmemnumb,clas_ysno='Y',clas_inst=datetime.now())

        
        try:
            new_data.save()  # 데이터 저장 시도
            return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
        except :
            # 저장에 실패한 경우 
            return HttpResponse(status=400, content=f"Fail save")


    @swagger_auto_schema(tags=['Class'], operation_id='강의수정 API', operation_description='강의수정', request_body=makeClassPutRequestSerializer)
    def put(self, request):
        clasnumb = request.data["clas_numb"] # 삭제 수정에는 필요, 등록일땐 빈칸
        tmemnumb = request.data["tmem_numb"] # 수강권번호
        user_numb = request.data["user_numb"] # ID값

        try:
            obj = TrClass.objects.get(clas_numb=clasnumb)
        except :
            return HttpResponse(status=404, content=f"No match data, {clasnumb}")

        clasname_v = request.data["clas_name"] # 강의이름
        clasdate_v = request.data['clas_date'] # 강의시작시간 
        clastime_v = request.data["clas_time"] # 수업시작시간 4자리 1130
        clasclos_v = request.data["clas_clos"] # 수업종료시간 4자리 1130
        clasnmax_v = request.data["clas_nmax"] # 정원 2자리
        claswait_v = request.data["clas_wait"] # 대기인원 2자리
        resvstat_v = request.data["resv_stat"] # 예약시작시간 12자리 202302011130
        resvlast_v = request.data["resv_last"] # 예약마감시간 12자리 202302211200
        resvalr1_v = request.data["resv_alr1"] # 예약마감전 알람시간 2자리 11시간

        # 모델 객체 생성 및 저장
        obj.clas_name = clasname_v
        obj.clas_date = clasdate_v
        obj.clas_time = clastime_v
        obj.clas_clos = clasclos_v
        obj.clas_nmax = clasnmax_v
        obj.clas_wait = claswait_v
        obj.resv_stat = resvstat_v
        obj.resv_last = resvlast_v
        obj.resv_alr1 = resvalr1_v
        obj.clas_updt = datetime.now()
        try:
            obj.save()  # 데이터 저장 시도
            return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
        except :
            # 저장에 실패한 경우 
            return HttpResponse(status=400, content=f"Fail update")


    @swagger_auto_schema(tags=['Class'], operation_id='강의삭제 API', operation_description='강의삭제', request_body=makeClassRequestSerializer)
    def DELETE(self, request):
        clasnumb = request.data["clas_numb"] # 삭제 수정에는 필요, 등록일땐 빈칸
        tmemnumb = request.data["tmem_numb"] # 수강권번호
        user_numb = request.data["user_numb"] # ID값

        try:
            obj = TrClass.objects.get(clas_numb=clasnumb)
        except :
            return HttpResponse(status=404, content=f"No match data, {clasnumb}")

        try:
            obj.delete()  # 데이터 저장 시도
            return HttpResponse(status=200)  # 성공적으로 저장된 경우 200 OK 응답 반환
        except :
            # 저장에 실패한 경우 400
            return HttpResponse(status=400, content=f"Fail delete")






# API : http://127.0.0.1:8000/callmembers/
# 통신방식 : GET
# 제목 : 강사회원 리스트
# 로직 : 강사의 회원권을 가져와서 모든 회원권의 회원 리스트를 보여준다
# 요청 : user_numb : 00000010, user_abcd = 'B'
# 리턴 : 강사의 회원 리스트, 기업의 강사 리스트
# @csrf_exempt
# @api_view(['GET'])
# def call_members(request):
class CallMembersAPI(APIView):
    @swagger_auto_schema(tags=['강사관리'], operation_id='강사회원 리스트 조회 API', operation_description='강사회원 리스트', responses={201:CallMembersSerializer})
    def get(self, request):
        if request.data["user_abcd"] == 'B': # 요청한사람이 강사인 경우
            # 강사의 회원 리스트
            usernumb = request.data["user_numb"] # ID값
            trmbsh_ob = TrMbship.objects.filter(user_numb=usernumb)# 강사 맴버쉽 가져오기
            # print(trmbsh_ob)
            user_dict = {} # 회원 중복 방지 -> 추후 강사-회원 테이블 만들어서 구조 변경
            for trmbsh in trmbsh_ob:
                tmemnumb = trmbsh.tmem_numb
                urmbsh_ob = UrMbship.objects.filter(tmem_numb = tmemnumb)
                for urmbsh in urmbsh_ob:
                    if urmbsh.user_numb not in user_dict:
                        user_dict[urmbsh.user_numb] = 1

            accumulated_queryset = UrMaster.objects.none()
            for key,values in user_dict.items():
                userdata_ob = UrMaster.objects.filter(user_numb = key)
                accumulated_queryset = accumulated_queryset | userdata_ob

            
            # 누적된 쿼리셋을 직렬화합니다.
            serializer = UrMasterSerializer(accumulated_queryset,many=True)
            return Response(serializer.data)
        
        elif request.data["user_abcd"] == 'C': # 요청한사람이 기업인 경우
            usernumb = request.data["user_numb"] # 회사 ID값
            urmbsh_ob = UrMaster.objects.filter(user_numb = usernumb)
            print(urmbsh_ob)

        else:
            return HttpResponse(400)
    

# API : http://127.0.0.1:8000/memberdetail/
# 통신방식 : GET
# 제목 : 회원관리의 회원 상세
# 로직 : 강사가 회원권에 등록한 회원리스트의 회원 디테일, 회원의 이전기록도 존재(정지이력)
# 요청 : user_numb : 00000010
# 리턴 : 강사의 회원정보 디테일
# @csrf_exempt
# @api_view(['GET'])
# def member_detail(request):
class MembersDetailAPI(APIView):
    @swagger_auto_schema(tags=['회원관리'], operation_id='회원관리의 회원 상세 API', operation_description='회원관리의 회원 상세', responses={201:MembersDetailSerializer})
    def get(self, request):
        data = request.data
        usernumb = data["user_numb"]
        accumulated_queryset = [] # 쿼리셋 쌓을곳

        sql_query = '''
        SELECT 
        B.user_numb,B.user_name, B.user_phon, A.UMEM_UNUM,A.UMEM_YSNO
        FROM ur_mbship A
        LEFT JOIN ur_master B ON A.user_numb = B.user_numb 
        WHERE A.user_numb =%s 
        ''' 
        
        params = [usernumb]
        
        with connection.cursor() as cursor:
            cursor.execute(sql_query, params)
            queryset = cursor.fetchall()
            accumulated_queryset += queryset


        return Response(accumulated_queryset)