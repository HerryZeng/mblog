from datetime import datetime

from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.


def index(request):
    template = get_template("ch08www/index.html")
    try:
        user_id = request.GET.get('user_id')
        user_pass = request.GET.get('user_pass')
        user_fcolor = request.GET.getlist('fcolor')
        byear = request.GET.get('byear')
    except:
        user_id = None

    if user_id != None and user_pass == '12345':
        verified = True
    else:
        verified = False

    years = range(1960, 2018)
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
