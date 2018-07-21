from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from todoapp.models import *
from todoapp.serialiser import *

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView


@csrf_exempt
def dislay(request):
    if request.method == 'GET':
        snippets = Todo_info.objects.values("task_title", "task_info", "actual_date", "status")
        serializer = TodoSerialiser(snippets, many=True)
        print("serialiser" + str(serializer.data))
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = TodoSerialiser(data=request.POST)
        import ipdb
        ipdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def modification_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        todorow = Todo_info.objects.get(pk=pk)
    except Todo_info.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TodoSerialiser(todorow)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerialiser(todorow, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todorow.delete()
        return HttpResponse(status=204)
