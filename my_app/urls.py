
from django.urls import path
from .views import *
from . import views 
app_name = 'my_app'
urlpatterns = [
#     path('login' ,Login.as_view()),
#     path('register' ,Register.as_view()),
#     path('user' ,UserAPI.as_view()),
#     path('refresh' ,RefreshAPI.as_view()),
#     path('logout' ,logoutAPI.as_view()),
#     path('forgot' ,forgotAPI.as_view()),
#     path('reset' ,resetAPI.as_view()),
#     path('deppartement' ,DeppartementList.as_view()),
#     path('categorie/' ,catagorieList.as_view()),
#     path('g/<str:pk>' ,categirieDetail.as_view()),
#     path('deppartement/<str:pk>' ,DepDetail.as_view()),
#     path('document' ,DocumentList.as_view()),
#     path('document/<str:pk>' ,DocumentDetail.as_view()),
      path('', views.index, name='index'),
      path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('specifics/<int:question_id>/', views.detail, name='detail'),
 ]
