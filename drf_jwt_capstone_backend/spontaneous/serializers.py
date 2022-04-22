from rest_framework import serializers
from .models import Explorer

class ExplorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Explorer
        fields = ['id','first_name', 'last_name','username', 'street', 'city', 'state', 'total_use' ]