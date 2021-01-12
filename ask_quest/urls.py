from django.urls import path  
from . import views  
  
app_name = 'ask_quest'  
  
urlpatterns = [  
    # post views  
    path('', views.index, name='ind'),  
    path('<int:chapter_id>/', views.detail, name='detail'),
    path('<int:question_id>/question/', views.question, name='question'),

    
    #path('resp/', views.detail2, name='detail2'),
    #path('resp3/', views.detail3, name='detail3'),
]
