from.views import todview,createview,deleteview,updateview
from django.contrib import admin
from django.urls import path
urlpatterns = [
    path('',todview),
    path('todo/create', createview,name='todo-create'),
    path('todo/<int:todo_id>/',deleteview,name='todo-delete'),
    path('todo/<int:todo_id>/update',updateview,name='todo-update'),
]
