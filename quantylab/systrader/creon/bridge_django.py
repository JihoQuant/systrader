import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quantylab.systrader.creon import Creon
from quantylab.systrader.creon import constants


c = Creon()


@csrf_exempt 
def handle_connection(request):
    if request.method == 'GET':
        # check connection status
        return JsonResponse(c.connected(), safe=False)
    elif request.method == 'POST':
        # make connection
        data = json.loads(request.body)
        _id = data['id']
        _pwd = data['pwd']
        _pwdcert = data['pwdcert']
        return JsonResponse(c.connect(_id, _pwd, _pwdcert), safe=False)
    elif request.method == 'DELETE':
        # disconnect
        return JsonResponse(c.disconnect(), safe=False)


def handle_stockcodes(request):
    c.wait()
    market = request.GET.get('market')
    if market == 'kospi':
        return JsonResponse(c.get_stockcodes(constants.MARKET_CODE_KOSPI), safe=False)
    elif market == 'kosdaq':
        return JsonResponse(c.get_stockcodes(constants.MARKET_CODE_KOSDAQ), safe=False)
    else:
        return HttpResponse('"market" should be one of "kospi" and "kosdaq".', status_code=400)


def handle_stockstatus(request):
    c.wait()
    stockcode = request.GET.get('code')
    if not stockcode:
        return HttpResponse('"code" should be provided.', status_code=400)
    res = c.get_stockstatus(stockcode)
    return JsonResponse(res)


def handle_stockcandles(request):
    c.wait()
    stockcode = request.GET.get('code')
    n = request.GET.get('n')
    if n:
        n = int(n)
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if not (n or date_from):
        return HttpResponse('Need to provide "n" or "date_from" argument.', status_code=400)
    res = c.get_chart(stockcode, target='A', unit='D', n=n, date_from=date_from, date_to=date_to)
    return JsonResponse(res, safe=False)


def handle_marketcandles(request):
    c.wait()
    marketcode = request.GET.get('code')
    n = request.GET.get('n')
    if n:
        n = int(n)
    date_from = request.GET.get('date_from')
    date_to = request.GET.get('date_to')
    if marketcode == 'kospi':
        marketcode = '001'
    elif marketcode == 'kosdaq':
        marketcode = '201'
    elif marketcode == 'kospi200':
        marketcode = '180'
    else:
        return HttpResponse('"code" should be one of "kospi", "kosdaq", and "kospi200".', status_code=400)
    if not (n or date_from):
        return HttpResponse('Need to provide "n" or "date_from" argument.', status_code=400)
    res = c.get_chart(marketcode, target='U', unit='D', n=n, date_from=date_from, date_to=date_to)
    return JsonResponse(res, safe=False)


def handle_stockfeatures(request):
    c.wait()
    stockcode = request.GET.get('code')
    if not stockcode:
        return HttpResponse('"code" should be provided.', status_code=400)
    res = c.get_stockfeatures(stockcode)
    return JsonResponse(res)


def handle_short(request):
    c.wait()
    stockcode = request.GET.get('code')
    n = request.GET.get('n')
    if n:
        n = int(n)
    if not stockcode:
        return HttpResponse('"code" should be provided.', status_code=400)
    res = c.get_shortstockselling(stockcode, n=n)
    return JsonResponse(res, safe=False)


def handle_investorbuysell(request):
    c.wait()
    stockcode = request.GET.get('code')
    n = request.GET.get('n')
    if n:
        n = int(n)
    if not stockcode:
        return HttpResponse('"code" should be provided.', status_code=400)
    res = c.get_investorbuysell(stockcode, n=n)
    return JsonResponse(res, safe=False)


def handle_marketcap(request):
    c.wait()
    res = []
    res += c.get_marketcap(target='2')  # 코스피
    res += c.get_marketcap(target='4')  # 코스닥
    return JsonResponse(res, safe=False)


def handle_holdingstocks(request):
    c.wait()
    res = c.get_holdingstocks()
    return JsonResponse(res, safe=False)


def handle_holdings(request):
    c.wait()
    res = c.get_holdings()
    return JsonResponse(res, safe=False)


def handle_balance(request):
    c.wait()
    res = c.get_balance()
    return JsonResponse(res, safe=False)
