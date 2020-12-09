from rest_framework import serializers
from .models import Recommend

class RecommendSerializers(serializers.ModelSerializer):
	class Meta:
		model = Recommend
		fields = '__all__'