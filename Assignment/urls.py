from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainApp.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




''' URLs for future API use...
    path('tokenDetails', views.tokenDetails, name="tokenDetails"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),'''
