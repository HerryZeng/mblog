from datetime import datetime

from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.


def index(request, tvno=3):
    tv_list = [{'name': '东森', 'tvcode': 'u5X_hiHtKkM'},
               {'name': '民视', 'tvcode': 'XxJKnDLYZz4'},
               {'name': '台视', 'tvcode': 'yk2CUjbyyQY'},
               {'name': '华视', 'tvcode': 'TL8mmew3jb8'}, ]

    template = get_template('video/index.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    html = template.render(locals())

    return HttpResponse(html)
