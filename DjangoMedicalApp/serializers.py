from rest_framework import serializers

from DjangoMedicalApp.models import Bill, Company, CompanyAccount, CompanyBank, Customer, CustomerRequest, Employee, EmployeeBank, EmployeeSalary, MedicalDetails, Medicine

class CompanySerliazer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"

class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyBank
        fields="__all__"
    
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerliazer(instance.company_id).data
        return response
    
class MedicineSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerliazer(instance.company_id).data
        return response

class MedicalDetailsSerliazer(serializers.ModelSerializer):
    class Meta:
        model=MedicalDetails
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['medicine']=MedicineSerliazer(instance.medicine_id).data
        return response
    
class EmployeeSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"

class CustomerSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

class BillSerliazer(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['customer']=CustomerSerliazer(instance.customer_id).data
        return response

class CustomerRequestSerliazer(serializers.ModelSerializer):
    class Meta:
        model=CustomerRequest
        fields="__all__"

class CompanyAccountSerliazer(serializers.ModelSerializer):
    class Meta:
        model=CompanyAccount
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerliazer(instance.company_id).data
        return response
    
class EmployeeBankSerliazer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeBank
        fields="__all__"

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['employee']=EmployeeSerliazer(instance.employee_id).data
        return response
  