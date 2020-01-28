from .models import AccessLog , Profile
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from .utils import get_date_time


def better_format(obj,time_type):
	if time_type == "entry":
		return str(obj.entry_time.date()) + " " + str(obj.entry_time.time())[:8]
	else:
		if obj.exit_time:
			return str(obj.exit_time.date()) + " " + str(obj.exit_time.time())[:8]
class ProfileSerailizer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		exclude = ["created_at"]

class EntryTimeSerializer(serializers.ModelSerializer):	
	profile_name = serializers.CharField(write_only=True)
	profile = ProfileSerailizer(read_only=True)
	entry_time = serializers.SerializerMethodField()
	exit_time = serializers.ReadOnlyField()
	class Meta:
		model = AccessLog
		fields = ['id','profile_name','profile','entry_time','exit_time']

	def create(self, validated_data):
		profile_name = validated_data.pop('profile_name')
		try:
			profile = Profile.objects.get(name=profile_name)
		except:
			raise NotFound("Profile Not Found")
		instance = AccessLog(profile = profile)
		instance.save()
		return instance
	
	def get_entry_time(self,obj):
		return better_format(obj,"entry")

class ExitTimeSerializer(serializers.ModelSerializer):
	profile_name = serializers.CharField(write_only=True)
	profile = ProfileSerailizer(read_only=True)
	entry_time = serializers.ReadOnlyField()
	exit_time = serializers.ReadOnlyField()
	class Meta:
		model = AccessLog
		fields = ['id','profile_name','profile','entry_time','exit_time']

	def create(self,validated_data):
		profile_name = validated_data.pop('profile_name')
		try:
			profile = Profile.objects.get(name=profile_name)
		except:
			raise NotFound("Profile Not Found")
		try:
			instance = AccessLog.objects.filter(profile=profile).latest('id')
		except:
			raise NotFound("This User has No Entry log present")
		if not instance.exit_time:
			instance.exit_time = get_date_time()
			instance.save()
		return instance

class AccessLogSerializer(serializers.ModelSerializer):
	profile = ProfileSerailizer(read_only=True)
	entry_time = serializers.SerializerMethodField()
	exit_time = serializers.SerializerMethodField()
	class Meta:
		model = AccessLog
		fields = "__all__"
	
	def get_entry_time(self,obj):
		return better_format(obj,'entry')
	
	def get_exit_time(self,obj):
		return better_format(obj,'exit')




