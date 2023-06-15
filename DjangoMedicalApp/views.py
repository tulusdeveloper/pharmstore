from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from DjangoMedicalApp.models import Company
from DjangoMedicalApp.serializers import CompanySerliazer

# Create your views here.
class CompanyViewSet(viewsets.ViewSet):

    def list(self,request):
        company=Company.objects.all()
        serializer=CompanySerliazer(company,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Company List Data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
        try:
            serializer=CompanySerliazer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Company Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Company Data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Company.objects.all()
            company=get_object_or_404(queryset,pk=pk)
            serializer=CompanySerliazer(company,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            dict_response={"error":False,"message":"Company Data Updated Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Updating Company Data"}

        return Response(dict_response)


company_list=CompanyViewSet.as_view({"get":"list"})
company_creat=CompanyViewSet.as_view({"post":"create"})
company_update=CompanyViewSet.as_view({"put":"update"})

