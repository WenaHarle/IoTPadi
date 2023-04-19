from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DataSerializer
from .models import Data
from django.http import JsonResponse


# Create your views here.
def create_data(request):
    day = request.GET.get('day')
    total = request.GET.get('total')
    avg = request.GET.get('avg')
    max = request.GET.get('max')
    min = request.GET.get('min')
    sumD = request.GET.get('sumD')
    Ourl = request.GET.get('Ourl')
    Purl = request.GET.get('Purl')


    data = Data.objects.create(
        day = day,
        total = total,
        avg = avg,
        max = max,
        min = min,
        sumD = sumD,
        Ourl = Ourl,
        Purl = Purl,
    )

    return JsonResponse({'success ;)': True, 'data_id': data.id})



@api_view(['GET'])
def ShowAll(request):
    datas = Data.objects.all()
    serializer = DataSerializer(datas, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewData(request, pk):
    datas = Data.objects.get(id=pk)
    serializer = DataSerializer(datas, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateData(request):
    serializer = DataSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateData(request, pk):
    data = Data.objects.get(id=pk)
    serializer = DataSerializer(instance=data, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteData(request, pk):
    data = Data.objects.get(id=pk)
    data.delete()

    return Response('Items delete successfully!')

