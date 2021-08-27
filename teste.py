from urllib.request import urlopen
import requests
import json

filme = input("Digite o nome do filme:");
q = filme.replace(" ","+");
url = "https://www.omdbapi.com/?s="+q+"&apikey=493b676d";
dados = urlopen(url).read();
dados1 = json.loads(dados);

print(dados1)
