from django.urls import path
from . import views 

urlpatterns = [
    # ex: /bucketlist/
    path('', views.index, name='index'),
    # ex: /bucketlist/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /bucketlist/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /bucketlist/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]