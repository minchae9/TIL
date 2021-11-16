from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)  # request.user.todos.all() 해도 같음
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    
    if not request.user.todos.filter(pk=todo_pk).exists():  # 내가 작성한 todo 목록에 수정하고자 하는 게 없으면
        return Response({'error': '권한이 없습니다.'})

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        todo.delete()
        return Response({ 'id': todo_pk })