from flask import Flask

app = Flask (__name__)

@app.route("/")
def homepage():                          #rotas
    return "<h1>Bem Vindo<h1>"

@app.route("/livros")
def livros():
    return '''
    <p>Livros<p>
        "ano_publicacao": 2018,
        "autor_id": "A1",
        "gênero": "Ficção",
        "preco": 45.9,
        "título": "O Segredo do Vale"
       
        "ano_publicacao": 2020,
        "autor_id": "A2",
        "gênero": "Ficção Científica",
        "preco": 59.9,
        "título": "Viagem ao Espaço"
        
        "ano_publicacao": 2015,
        "autor_id": "A3",
        "gênero": "Mistério",
        "preco": 35.5,
        "título": "Histórias Perdidas"
    }
}
'''

@app.route("/autores")
def autores():
    return '''
    <p>Autores<p>
        "ano_nascimento": 1980,
        "nacionalidade": "Brasileira",
        "nome": "Clara Mendes",
        "obras_notáveis": [
            "O Segredo do Vale",
            "Noites de Verão"
   
        "ano_nascimento": 1975,
        "nacionalidade": "Italiano",
        "nome": "Marco Russo",
        "obras_notáveis": [
            "Viagem ao Espaço",
            "O Código das Estrelas"

        "ano_nascimento": 1990,
        "nacionalidade": "Mexicana",
        "nome": "Elena Torres",
        "obras_notáveis": [
            "Histórias Perdidas",
            "O Enigma do Passado"
'''

@app.route("/clientes")
def clientes():
    return '''
    <p>Clientes<p>

        "ano_nascimento": 1980,
        "nacionalidade": "Brasileira",
        "nome": "Clara Mendes",
        "obras_notáveis": [
            "O Segredo do Vale",
            "Noites de Verão"

        "ano_nascimento": 1975,
        "nacionalidade": "Italiano",
        "nome": "Marco Russo",
        "obras_notáveis": [
            "Viagem ao Espaço",
            "O Código das Estrelas"

        "ano_nascimento": 1990,
        "nacionalidade": "Mexicana",
        "nome": "Elena Torres",
        "obras_notáveis": [
            "Histórias Perdidas",
            "O Enigma do Passado"
'''
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")