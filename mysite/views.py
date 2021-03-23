from django.shortcuts import render
from datetime import datetime


def index(request, tvno = 0):
    tv_list = [{'name':'潤羽露西婭', 'tvcode':'rPKcmD1QIds'},
               {'name':'戌神沁音', 'tvcode':'Fz-FoyXvBPo'},
               {'name':'peko', 'tvcode':'HuqlqDCjqHo'},]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tvno = tvno
    tv = tv_list[tvno]
    return render(request, 'index.html', locals())