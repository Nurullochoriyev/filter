
from django.urls import path


from .views import *
urlpatterns = [

    path('index/',index,name='home'),
    path('index/',index,name='index'),
    path('add_news/', add_news, name='add_news'),
    path('category/<int:id>/',category,name='category'),
    path('about_new/<int:new_id>/',about_new,name='about_new'),
    # path('update_new/<int:new_id>/',update_new,name='update_new'),
    path('delete/<int:new_id>/',delete,name='delete'),
    path('',loginPage,name='login'),

]