from django.urls import path, include
from rest_framework import routers
from .views import login_api, logout_api, register_api, profile_api

router = routers.DefaultRouter()
#router.register(r'records', RecordViewSet)

urlpatterns = [
    #path('api/', include(router.urls)),
    path('api-auth/login/', login_api, name='login'),
    path('api-auth/logout/', logout_api, name='logout'),
    path('api-auth/register/', register_api, name='register'),
    path('api-auth/profile/', profile_api, name='profile')
]
