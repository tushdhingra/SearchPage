from rest_framework import serializers
from .models import profile

class profileSerializer(serializers.ModelSerializer):
	class Meta:
		model = profile
		fields = '__all__'