
from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('stu',views.SaveData.as_view(),name="stu_form"),
    path('update<int:id>/',views.Update_post.as_view(),name='Update_post'),
    path('show<int:id>/',views.Student_data_Show.as_view(),name='show_data'),
    path('stu_data',views.StudetdataView.as_view(),name="stu_data"),
    
]
