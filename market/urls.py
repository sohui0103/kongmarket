from django.urls import path 
from market.views import * 
urlpatterns = [ 
	path('', home, name='home'), #홈화면
]