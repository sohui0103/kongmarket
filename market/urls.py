from django.urls import path 
from market.views import * 
urlpatterns = [ 
	#메인화면
    path('', home, name='home'),

    #중고거래
    path('market/', home, name='market'),
    path('detail/<int:blog_id>/', detail, name='detail'),     
    path('create/', create, name='create'),
    path('update/<int:blog_id>/', update, name='update'),
    path('search', search, name='search'),
    path('delete/<int:blog_id>', delete , name="delete"),

    #약속 구해요
    path('promise/', home, name='promise'),

    #채팅방
    path('chat/', home, name='chat'),
]