from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.utils.dateparse import parse_date
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from .models import UserDetail, PlotHistory
from .serializers import PlotHistorySerializer
from .utils import add_plot_or_400, delete_plot_or_404


# Main Page
@login_required(login_url='/login')
def mainPage(request):
    return render(request, "mainApp/mainPage.html")


@api_view(['POST'])
@permission_classes((AllowAny, ))
def createUser(request, format=None):
    parser=(MultiPartParser,)
    params=request.data
    print(params)
    obj, notif=User.objects.get_or_create(username=params['email'], email=params['email'])
    obj.set_password(params['pass'])
    print(notif, obj)
    if(notif):
        obj.save()
        obj.first_name=params['fname']
        obj.last_name=params['lname']
        obj.save()
        date = parse_date(params['dob'])
        obj1, notif1=UserDetail.objects.get_or_create(
                        user=User.objects.get(username=params['email']),
                        gender=params['gender'],
                        phone=params['phone'],
                        country=params['country'],
                        city=params['city'],
                        state=params['state'],
                        dob=date,
                        photo=params['file'])
        print(notif1)
        if(notif1):
            obj1.save()
            return Response({"message":"Successfully Created User", "status":"201"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def validateUser(request):
    params=request.data
    user=authenticate(username=params['username'], password=params['pass'])
    print(user)
    if(user is not None):
        login(request, user)
        return Response({"message":"Successfully Logged In", "status":"200"}, status=status.HTTP_200_OK)
    else:
        return Response({"message":"No Such User Exists", "status":"404"})


class historyManagement(APIView):

    #GET History
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        try:
            list=PlotHistory.objects.filter(user=request.user)
            serializer=PlotHistorySerializer(list, many=True)
            return Response({"message":"Successfully Retrieved History", "list":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Some Unexpected Error Occured"}, status=status.HTTP_400_BAD_REQUEST)


    permission_classes=(IsAuthenticated,)
    # Plot SAVE
    def post(self, request, format=None):
        parser_classes = (JSONParser,)
        obj,status1=add_plot_or_400(request)
        if(status1==201):
            serializer= PlotHistorySerializer(obj)
            return Response({'message':"Successfully Saved Plot", "details":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':"Error"}, status=status.HTTP_400_BAD_REQUEST)


    permission_classes=(IsAuthenticated,)
    # Plot Delete
    def delete(self, request, format=None):
        parser_classes = (JSONParser,)
        status1=delete_plot_or_404(request)
        if(status1==200):
            return Response({'message':"Successfully Deleted Plot History"}, status=status.HTTP_200_OK)
        else:
            return Response({'message':"Error"}, status=status1)
