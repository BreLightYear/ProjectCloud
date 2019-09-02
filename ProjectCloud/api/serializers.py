from rest_framework import serializers

class EmpresaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)