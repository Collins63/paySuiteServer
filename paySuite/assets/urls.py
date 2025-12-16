from django.urls import path , include
from .views import CompanyAssestViewset , AssetLinksViewset
from rest_framework.routers import DefaultRouter

companyAssetsRouter = DefaultRouter()
companyAssetsRouter.register(r'companyAssets' , CompanyAssestViewset , basename='companyAssets')

assetLinksRouter = DefaultRouter()
assetLinksRouter.register(r'assetLinks' , AssetLinksViewset, basename='assetLinks' )

urlpatterns = [
    path('api/' , include(companyAssetsRouter.urls)),
    path('api/' , include(assetLinksRouter.urls))
]
