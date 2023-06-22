from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny
from .models import Record
from .serializers import RecordSerializer, MyUserSerializer

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
@ensure_csrf_cookie
def login_api(request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(request=request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({"detail": "Login Successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(["GET"])
@ensure_csrf_cookie
def logout_api(request):
    logout(request)
    return Response({"detail": "Logout Successful"}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def register_api(request):
    serializer = MyUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({"detail": "Registration Successful"}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@login_required
def profile_api(request):
    serializer = MyUserSerializer(request.user)
    return Response(serializer.data)


# class IsMemberOfRecordAdder(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='Record Adder').exists()
#
#
# class IsMemberOfDataViewer(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.groups.filter(name='Data Viewer').exists()
#
#
# class RecordViewSet(viewsets.ModelViewSet):
#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated, IsMemberOf]
#
#     def get_permissions(self):
#         if self.action == 'create':
#             permission_classes = [IsAuthenticated, IsMemberOfRecordAdder]
#         else:
#             permission_classes = [IsAuthenticated, IsMemberOfDataViewer]
#
#         return [permission() for permission in permission_classes]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)