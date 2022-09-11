from django.urls import path 
from account.views import * 
from account import views as accounts_views

urlpatterns = [ 
	path('login/', accounts_views.login, name='login'),
	path('logout/', accounts_views.logout, name='logout'),
	path('signup/', signup, name='signup'),
]