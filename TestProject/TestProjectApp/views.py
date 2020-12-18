
from django.shortcuts import render
from datetime import datetime,date


def hello(request):
	
	#today = datetime.datetime.now().date()
	today  = date.today()

	return render(request,"hello.html",{"today":today})	
