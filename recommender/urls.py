'''from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.RecommendView)
urlpatterns = [
	#path('form/', views.myform, name='myform'),
    #path('api/', include(router.urls)),
    #path('status/', views.Recommendations),
    path('form/', views.userpreferenceForm,name = 'userpreference'),
 
] 