from rest_framework import serializers
from .models import Department, Subject, Teacher, Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'department', 'department_name']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'department', 'department_name', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password', 'default123')
        user = User(**user_data)
        user.set_password(password)
        user.save()
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            if 'password' in user_data and user_data['password']:
                user.set_password(user_data['password'])
            user.save()
            
        instance.department = validated_data.get('department', instance.department)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'user', 'roll_number', 'department', 'department_name', 'phone', 'address']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password', 'default123')
        user = User(**user_data)
        user.set_password(password)
        user.save()
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            if 'password' in user_data and user_data['password']:
                user.set_password(user_data['password'])
            user.save()
            
        instance.roll_number = validated_data.get('roll_number', instance.roll_number)
        instance.department = validated_data.get('department', instance.department)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
