from django.urls import path
from . import views

urlpatterns = [
    path('getCumulativeScore',views.GetCumulativeScore.as_view(),name="get-cumulative-score"),
    path('studentDetails', views.StudentDetails.as_view(), name="student-details"), 
    path('getQuizScore/<int:quizId>', views.getQuizScore.as_view(), name="student-details"),  
    path('getPeerResponse/<int:quizId>', views.getPeerResponse.as_view(), name="peer-details"),  
    # path('doSelfAssessment/<int:quizId>', views.doSelfAssessment.as_view(), name="student-details"), 
    path('putSelfResponse/<int:quizId>',views.putSelfResponse.as_view(),name="put-self-data"),
    path('putPeerResponse/<int:quizId>',views.putPeerResponse.as_view(),name="put-peer-data"),
    path('addstudent',views.addstudent.as_view(),name="addstudent"),

]