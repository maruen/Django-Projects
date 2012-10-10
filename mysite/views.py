from django.template import Template,Context
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now
#    return HttpResponse(html)

def hours_ahead(request,offset):
    hours_offset = int(offset)
    hours_ahead  = datetime.datetime.now() + datetime.timedelta(hours=hours_offset)
    return render_to_response('hours_ahead.html', locals())


#def current_datetime(request):
#    now = datetime.datetime.now()
#    fp = open('home/maruen/templates/mytemplate.html')
#    t = Template(fp.read())
#    fp.close()
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)


#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

#def current_datetime(request):
#    now = datetime.datetime.now()
#    return render_to_response('current_datetime.html',{'current_date':now})


def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())














