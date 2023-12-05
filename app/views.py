from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class ProductData(ViewSet):
    def list(self,request):
        PD=Product.objects.all()
        JD=ProductModelSerializer(PD,many=True)
        return Response(JD.data)
    
    def retrieve(self,request,pk):
        PD=Product.objects.get(Pid=pk)
        JD=ProductModelSerializer(PD)
        return Response(JD.data)
    
    def create(self,request):
        
        JD=request.data
        PD=ProductModelSerializer(data=JD)
        if PD.is_valid():
            PD.save()
            return Response({"Message":"Data Inserted Successfully"})
        else:
            return Response({"Message":"There is Some Validation Issue"})
        
    def update(self,request,pk):
        PD=Product.objects.get(Pid=pk)
        JD=ProductModelSerializer(PD,data=request.data)
        if JD.is_valid():
            JD.save()
            return Response({"Message":"Data is Updated Successfully"})
        else:
            return Response({"Message":"There is an some Validation Issue"})
        
    def partial_update(self,request,pk):
        PD=Product.objects.get(Pid=pk)
        JD=ProductModelSerializer(PD,data=request.data,partial=True)
        if JD.is_valid():
            JD.save()
            return Response({"Message":"Data Updated Successfully"})
        else:
            return Response({"Message":"There is Some Validation Issue"})
        
    def destroy(self,request,pk):
        PD=Product.objects.get(Pid=pk)
        PD.delete()
        return Response({"Message":"Data Deleted Successfully!!!!!!"})
    
  
