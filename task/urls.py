from django.urls import path

from .views import *


urlpatterns = [
    path('', TaskView.as_view(), name='tasks_list_url'),
    path('<str:id>/complete/', TaskComplete.as_view()),
    path('<str:id>/delete/', TaskDelete.as_view())
]