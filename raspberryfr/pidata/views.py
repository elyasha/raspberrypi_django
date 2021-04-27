from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

def visualizar_dados(request):

    # fazer oque vc quiser

    return render(request, "pidata/dados.html")


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


        # Criar uma nova leitura de dados

        # Dar o timestamp
    return redirect("home")
