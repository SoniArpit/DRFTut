from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    # name = serializers.CharField(read_only=True)

    # validators
    # validators -  reusable (1st priority to check by is_valid() in view)
    def no_space_name(value):
        for s in value:
            if s.isspace():
                raise serializers.ValidationError("Space not allowed")
        return value

    name = serializers.CharField(max_length=100, validators=[no_space_name])

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

        # read_only in multiple fields
        # read_only_fields = ['name', 'roll']

        # extra_kwargs = {'name': {'read_only': True}}

    # field level validation (2nd priority to check by is_valid() in view)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    # object level validation (3rd priority to check by is_valid() in view)
    def validate(self, data):
        print(data)
        nm = data.get("name")
        ct = data.get("city")
        print(nm)
        if nm != nm.capitalize() or ct != ct.capitalize():
            raise serializers.ValidationError("First letter must be capital")
        return data
