from rest_framework.decorators import api_view,renderer_classes,permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated,AllowAny
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def categories_list(request):
    categories = Categories.objects.all().order_by("-id")
    serializers = CategoriesSerializer(categories,many=True)
    return Response(serializers.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_create(request):
    serializers = CategoriesSerializer(data=request.data,context={'request':request})
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def categories_detail(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    serializers = CategoriesSerializer(category)
    return Response(serializers.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_update(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    serializers = CategoriesSerializer(category, data=request.data, context={'request': request})
    
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_delete(request,pk):
    category = get_object_or_404(Categories,pk=pk)
    category.delete()
    return Response({"detail":"Category delete Sucessfully."},
    status=status.HTTP_200_OK)