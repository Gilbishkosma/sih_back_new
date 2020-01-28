from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .models import AccessLog
from .serializers import EntryTimeSerializer , ExitTimeSerializer , AccessLogSerializer
from django.db.models import Q
from twilio.rest import Client
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



account_sid = 'ACd5982c56d7de81915fdb6863ba6a2630'
auth_token = '0f26b5f3b6b47cbed0ed15185dc07aa9'
client = Client(account_sid, auth_token)

def send(recipient, msg):
    message = client.messages \
                    .create(
                         body=str(msg),
                         from_='+12018906793',
                         to=str(recipient)
                     )



class EntryTimeView(ListCreateAPIView):
	queryset = AccessLog.objects.all().order_by('-entry_time')
	serializer_class = EntryTimeSerializer

	def get_queryset(self):
		only_entry = self.request.GET.get('only_entry',False)
		queryset = self.queryset.all()
		if only_entry:
			queryset = self.queryset.filter(exit_time = None)
		return queryset

entry_create_view = EntryTimeView.as_view()


class ExitTimeView(ListCreateAPIView):
	queryset = AccessLog.objects.all().order_by('-exit_time')
	serializer_class = ExitTimeSerializer

exit_create_view = ExitTimeView.as_view()



class AccessLogView(ListAPIView):
	queryset = AccessLog.objects.all().order_by('-id')
	serializer_class = AccessLogSerializer

	def get_queryset(self):
		date = self.request.GET.get('date',False)
		search = self.request.GET.get('search',False) 
		queryset = self.queryset.all()
		if date:
			queryset = self.queryset.filter(entry_time__date=date)
			if search:
				queryset = queryset.filter(Q(profile__name__icontains=search) | Q(profile__designation__icontains=search))
				return queryset
		if search:
			queryset = self.queryset.filter(Q(profile__name__icontains=search) | Q(profile__designation__icontains=search))
		return queryset

access_log = AccessLogView.as_view()


class EmergencyMsgView(APIView):

	def post(self,request):
		msg = self.request.data.get('message')
		access_log = AccessLog.objects.filter(exit_time = None)
		for person in access_log:
			if person.profile.phone_no:
				send(person.profile.phone_no,msg)
		return Response({'status':status.HTTP_201_CREATED})

emergency_view = EmergencyMsgView.as_view()