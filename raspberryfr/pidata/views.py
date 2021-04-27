from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from raspberryfr.pidata.models import Medida1

import json

# Create your views here.

def visualizar_dados(request):

    # fazer oque vc quiser
    medidas = Medida1.objects.all()

    return render(request, "pidata/dados.html", context={"medidas": medidas})


@csrf_exempt
def receber_dados(request):

    if request.method == "POST":
        # processar os dados
        print("Recebi um POST")

        print(request.body.decode())
        string_json = request.body.decode()
        objeto_json = json.loads(string_json)
        print(objeto_json)

        print("Tensão elétrica é de {}".format(objeto_json["tensao"]))
        print("Corrente elétrica é de {}".format(objeto_json["corrente"]))

        medida1 = Medida1.objects.create(tensao_eletrica=objeto_json["tensao"])
        medida1.save()
        # Criar uma nova leitura de dados

        # Dar o timestamp
    return redirect("home")
