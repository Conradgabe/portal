from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.commentList.as_view()),
    path('comment/<str:pk>', views.commentDetail.as_view())

]