from django.contrib.auth.models import User
from rest_framework import serializers
from tvseries.serializers import Serieslizer


class UserSerializer(serializers.ModelSerializer):
	seria = Serieslizer(many=True,read_only=True)
	
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'seria', )