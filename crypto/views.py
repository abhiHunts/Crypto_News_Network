from django.shortcuts import render

def home(request):
    import requests
    import json

    # Grab Crypto Prices 
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,USDC,XRP,BUSD,ADA,DOGE,MATIC&tsyms=USD,INR,EUR')
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
   
    return render(request, 'home.html', {'api':api, 'price':price})

def prices(request):

    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD,INR,EUR')
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        notfound = 'Enter a Crypto Currency Symbol in above form!'
        return render(request, 'prices.html', {'notfound':notfound})