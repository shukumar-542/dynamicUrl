import re
from django.shortcuts import render

# Create your views here.

def home(request):
      return render(request,'enroll/home.html')

# def show_details(request,my_id):
#       student ={'id': my_id}
#       return render(request, 'enroll/show.html',student)


def show_details(request, my_id):
      if my_id == 1:
            student ={'id':my_id, 'name':'shukumer'}

      return render(request, 'enroll/show.html',student)


def showSubDetails(request, my_id, sub_id):
      if(my_id == 1 and sub_id == 2):
            subStudent = {'id':my_id, 'sid':sub_id, 'name':'shukumar ghosh'}
      if(my_id == 1 and sub_id == 3):
            subStudent = {'id':my_id, 'sid':sub_id, 'name':'jahanur'}
      
      return render(request, 'enroll/show.html',subStudent)
