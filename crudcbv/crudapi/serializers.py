from rest_framework import serializers
from .models import Student

# validators -  reusable (1st priority to check by is_valid() in view)


def no_space_name(value):
    for s in value:
        if s.isspace():
            raise serializers.ValidationError("Space not allowed")
    return value


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[no_space_name])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)

        instance.save()
        return instance

    # field level validation (2nd priority to check by is_valid() in view)
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError("Sear Full")
        return value

    # object level validation (3rd priority to check by is_valid() in view)
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        real_nm = nm
        real_ct = ct
        print(nm.capitalize())
        print(nm)

        if nm != nm.capitalize() or ct != ct.capitalize():
            raise serializers.ValidationError("First letter must be capital")
        return data