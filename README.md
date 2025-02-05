<h2>📌 O que é um ambiente virtual (<code>venv</code>)?</h2>
<p>Um ambiente virtual (<code>venv</code>) é um ambiente isolado que permite instalar pacotes Python sem afetar a instalação global do sistema. Isso é útil para manter dependências organizadas e evitar conflitos entre projetos.</p>

<h2>🛠 Criando um ambiente virtual</h2>
<p>Para criar um ambiente virtual em Python, use o seguinte comando:</p>
<pre><code>python -m venv venv</code></pre>
<p>Isso criará uma pasta chamada <code>venv</code> com todos os arquivos necessários.</p>

<h2>▶️ Ativando o ambiente virtual</h2>
<h3>🖥 Windows (PowerShell):</h3>
<pre><code>.\venv\Scripts\Activate.ps1</code></pre>
<p>Se ocorrer um erro, talvez seja necessário modificar a permissão de execução de scripts:</p>
<pre><code>Set-ExecutionPolicy RemoteSigned</code></pre>

<h3>🐧 Linux/macOS:</h3>
<pre><code>source venv/bin/activate</code></pre>

<h2>📦 Instalando pacotes dentro do venv</h2>
<p>Após ativar o ambiente virtual, você pode instalar pacotes normalmente com <code>pip</code>:</p>
<pre><code>pip install flask</code></pre>

<h2>🚀 Executando um script Python</h2>
<p>Se quiser rodar um arquivo Python dentro do ambiente virtual:</p>
<pre><code>python nome_do_arquivo.py</code></pre>
<p>Se rodar esse comando sem ativar o <code>venv</code>, o script será executado com a versão global do Python, podendo gerar erros caso os pacotes necessários não estejam instalados.</p>

<h2>❌ Desativando o ambiente virtual</h2>
<p>Para sair do ambiente virtual, use:</p>
<pre><code>deactivate</code></pre>

<h2>📌 Conclusão</h2>
<p>Ambientes virtuais são essenciais para organizar dependências em projetos Python. Criar, ativar e instalar pacotes no <code>venv</code> é simples e evita problemas de compatibilidade entre projetos diferentes.</p>

<hr>
