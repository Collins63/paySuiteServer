from rest_framework import serializers
from .models import SalaryComponents ,SalaryGrades , SalaryGradeComponents

class SalaryComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryComponents
        fields = '__all__'
        
class SalaryGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryGrades
        fields = '__all__'
        
class SalaryGradeComponentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryGradeComponents
        fields = '__all__'
        
