from django.shortcuts import render
from django.db.models.functions import Lower
from testapp import views
from testapp.models import Employee
from django.db.models import Q
# Create your views here.
def retreve_view(request):
  #emp_list=Employee.objects.all()
  print("Hello Vikram Abid")
  emp_list = Employee.objects.all().order_by('ename')


  #emp_list = Employee.objects.filter(esal__gt=15000)
  #emp_list = Employee.objects.filter(esal__gte=15000)
  #emp_list = Employee.objects.filter(ename__contains="John")
  #emp_list = Employee.objects.filter(id__in=[1,3,5])
  #emp_list = Employee.objects.all.only('ename','esal')
  print(type(emp_list))
  return render(request,'testapp/index.html',{'emp_list':emp_list})
from django.db.models import Avg,Sum,Max,Min,Count
def display_view(request):
  avg=Employee.objects.all().aggregate(Avg('esal'))
  max = Employee.objects.all().aggregate(Max('esal'))
  min = Employee.objects.all().aggregate(Min('esal'))
  sum = Employee.objects.all().aggregate(Sum('esal'))
  count = Employee.objects.all().aggregate(Count('esal'))
  my_dict={'avg':avg,'max':max['esal__max'],'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
  return render(request,'testapp/aggregate.html',my_dict)
