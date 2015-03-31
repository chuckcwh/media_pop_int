import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from media_pop_app.models import KeyCombo


def index(request):
    KeyCombo.objects.get_or_create(ctrl=True,keychar="C",meaning="copy")
    KeyCombo.objects.get_or_create(keychar="X",meaning="self-defined function 1")
    KeyCombo.objects.get_or_create(shift=True,ctrl=True,keychar="G",meaning="self-defined function 2")
    return render_to_response('index.html')


@csrf_exempt
def getKeys(request):
    keycombo = []
    if request.method == "GET":
        keys = KeyCombo.objects.all()
        for key in keys:
            shift = alt = ctrl = meta = ""
            if key.shift:
                shift = 'shift + '
            if key.alt:
                alt = 'alt + '
            if key.ctrl:
                ctrl = 'ctrl + '
            if key.meta:
                meta = 'meta + '
            keycombo.append([shift + alt + ctrl + meta + key.keychar, key.meaning])
    return HttpResponse(json.dumps(keycombo), content_type='application/json')


@csrf_exempt
def keySet(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            obj = KeyCombo.objects.get(shift=data['shiftKey'],
                                       meta=data['metaKey'],
                                       ctrl=data['ctrlKey'],
                                       alt=data['altKey'],
                                       keychar=data['comboParts'][-1]['keyChar'])
            action = obj.meaning
        except:
            action = "Not in the library"
    else:
        action = "Internal Error"
    return HttpResponse(json.dumps(action), content_type='application/json')
