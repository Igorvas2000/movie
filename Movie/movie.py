from urllib.request import urlopen
import requests
import json

filme = input("Digite o nome do filme:");
q = filme.replace(" ","+");
url = "https://www.omdbapi.com/?s="+q+"&apikey=493b676d";
dados = urlopen(url).read();
dados1 = json.loads(dados);

Movie_add = open("Movie.html","w");

for Search in dados1['Search']:
    html = """
    <html lang="en">
<head>
    <title>Filme</title>
    <style>
        body{
            background: white;
        }
        table{
            background: black;
            width: 350px;
            margin-top: 100px;
            border-color: silver;
        }
    </style>
</head>
<body text="white">
    <center>
        <img src="""+Search['Poster']+"""/>
        <table border="10" color='#0C4940'>
            <tr>
                <td>Nome: """+Search['Title']+"""</td>
            </tr>
        
        <tr>
            <td>Ano Lançamento: """+Search['Year']+"""</td>
        </tr>

        
        <tr>
            <td>ID: """+Search['imdbID']+"""</td>
        </tr>

        <tr>
            <td>Tipo: """+Search['Type']+"""</td>
        </tr>
        

        </table>
    </center>
    
</body>
</html>
"""
Movie_add.write(html);
Movie_add.close();
