from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    list = ["http://1.soompi.io/wp-content/uploads/2015/02/IU.jpg"]
    img = random.choice(list)
    context = {'src': img}
    return render (request, "base/index.html", context)

def result(request):
    type=request.GET["type"]
    level=request.GET["level"]

    korean = {'Jogeum' : ['GomTangEee', 'Myunga', 'JangWon'], 'Jotna' : ['BonChon', 'BBQ', 'Chugajib']}
    american = {'Jogeum' : ['Ihop', 'SevenEleven', 'Mcdonald'], 'Jotna' : ['GoldenCorral', 'FiveGuys','SmokeDatGrass']}
    other = {'Jogeum' : ['Pho', 'Redo', 'PandaExpress'], 'Jotna' : ['ManassasHibachi', 'ChantillyHibachi', 'Oolalala']}

    n = type
    while True:
        if n == '':
            print('DumbFuck type korean or american or other')
            n = type
        else:
            x = level
            while True:
                if n == 'korean' and x == 'jogeum' :
                    result=random.choice(korean['Jogeum'])
                    break
                elif n == 'korean' and x == 'jotna' :
                    result=random.choice(korean['Jotna'])
                    break
                elif n == 'american' and x == 'jogeum' :
                    result=random.choice(american['Jogeum'])
                    break
                elif n == 'american' and x == 'jotna' :
                    result=random.choice(american['Jotna'])
                    break
                elif n == 'other' and x == 'jogeum' :
                    result=random.choice(other['Jogeum'])
                    break
                elif n == 'other' and x == 'jotna' :
                    result=random.choice(other['Jotna'])
                    break
            break

    context = {'restaurant': result}
    return render(request, "base/result.html", context)
