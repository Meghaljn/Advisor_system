from django.shortcuts import render
#from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.contrib.auth import login


from .models import advisors,booking
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

#from .serializers import usersSerializer
from .serializers import advisorsSerializer,bookingSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def post_advisors(request):
    if request.method == 'POST':
        advisors_data = JSONParser().parse(request)
        advisors_serializer = advisorsSerializer(data=advisors_data)
        if advisors_serializer.is_valid():
            #advisor.save()
            advisors_serializer.save()
            return JsonResponse(advisors_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(advisors_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_list(request,id):
    if request.method == 'GET':
        all_advisors =  advisors.objects.all()
        serializer = advisorsSerializer(all_advisors,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

@api_view(['GET','POST'])
def book_time(request,user_id, advisor_id,):
    if request.method == 'POST':
        booking_date_time = request.data['booking_date_time']
        booking_data = {'user_id': user_id, 'advisor_id': advisor_id,'booking_date_time': booking_date_time  }
        booking_serializer = bookingSerializer(data=booking_data)
        if booking_serializer.is_valid():
            booking_serializer.save()
            return JsonResponse(booking_serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_booked_list(request,user_id):
    if request.method == 'GET':
        all_advisors = advisors.objects.all()
        arr_list = []
        for advisor in all_advisors:
            arr_ele = {}
            advisor_serializer = advisorsSerializer(advisor)
            arr_ele['advisor'] = advisor_serializer.data
            try:
                obj = booking.objects.get(advisor_id = advisor.id)
                if obj:
                    arr_ele['booking_date_time'] = obj.booking_date_time
                    arr_ele['booking_id'] = obj.id
                    arr_list.append(arr_ele)
            except :
                arr_list.append(arr_ele)
                continue

        return JsonResponse(arr_list,safe = False)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user_id" : user.id,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            "user_id" : user.id,
            "token" : AuthToken.objects.create(user)[1]
        })
       
