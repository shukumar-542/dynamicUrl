from django.urls import path
from enroll import views

urlpatterns = [
    path('student/<int:my_id>/', views.show_details, name='details'),
    path('student/<int:my_id>/<int:sub_id>', views.showSubDetails, name='subDetails')


]