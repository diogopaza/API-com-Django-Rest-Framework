# API-com-Django-Rest-Framework

<h3>Para rodar a aplicação desenvolvida via Docker:</h3>
<p>É possível executar a aplicação diretamente via container docker com o comando abaixo, importante lembrar que a porta 8000 da maquina onde sera executada a aplicacao nao pode estar em uso.</p>
<p><strong>docker run -p 8000:8000 diogopaza/api-saude-django-rest</strong></p>

<h3>Para rodar a aplicação desenvolvida via download do GitHub:</h3>
<p>Clonar o repositorio:</p>
<p><strong>git clone https://github.com/diogopaza/API-com-Django-Rest-Framework</strong></p>
<p>Acessar a pasta do projeto</p>

<h3>Frameworks:</h3>
<ul>
  <li>Django</li>
  <li>Django Rest Framework</li>
</ul>
 <h4>Rotas da Pessoa Profissional</h4>
 <p><strong>Verbo GET</strong> <br>
   http://127.0.0.1:8000/pessoa-profissional/ - listar todas as Pessoas Profissionais cadastradas.</p>
   <p><strong>Verbo POST</strong> <br>
   http://127.0.0.1:8000/pessoa-profissional/ - rota para cadastrar uma nova Pessoa Profissional. Campo cpf, possue validação através da biblioteca validate-docbr, com isso é necessário passar um cpf válido para cadastrar a pessoa profissional, bem como o celular também possue validação sendo necessário um celular como este: 11 88855-4444.</p>
  
  
    {
      "nome": "diogo",
      "nome_social": "diogo-teste",
      "cpf": "56630352068",
      "celular": "45 99999-55511",
      "especialidade": "medico",
      "idade": 23,
      "data_nascimento": "1990-05-06"
    }

  <p><strong>Verbo PATCH</strong> <br>
   http://127.0.0.1:8000/pessoa-profissional/idDaPessoaProfissional/ -  rota para atualizar os dados de uma  Pessoa Profissional. </p>
   <p><strong>Verbo DELETE</strong> <br>
   http://127.0.0.1:8000/pessoa-profissional/idDaPessoaProfissional/ - rota para excluir uma  Pessoa Profissional. </p>

   <h3>Rotas para a entidade Consulta</h3>
  <p><strong>Verbo GET</strong> <br>
   http://localhost:8000/consultas/ - listar todas as Consultas cadastradas.</p>
    <p><strong>Verbo POST</strong> <br>
   http://127.0.0.1:8000/consultas/ - rota para cadastrar uma nova Consulta. O Json abaixo mostra o formato com os campos necessários para incluir uma nova consulta, sendo necessário uma data e um id de uma Pessoa Profissional cadastrada.</p>

   ```
  {
    "data_consulta": "2023-11-18",
    "pessoa_profissional": "5526fc9d-b714-42d6-9225-c00f4873da77"
  }
 ```

<p><strong>Verbo PATCH</strong> <br>
   http://127.0.0.1:8000/consultas/idDaConsulta/ - rota para atualizar os dados de uma Consulta. </p>
   <p><strong>Verbo DELETE</strong> <br>
   http://127.0.0.1:8000/consultas/idDaConsulta/ - rota para excluir uma Consulta. </p>

   <h3>Consultar todas as consultas de uma Pessoa Profissional</h3>
   <p><strong>Verbo GET</strong> <br>
   http://127.0.0.1:8000/consultas-por-profissional/idDoProfissional/ - rota para buscar todas as consultas de um profissional, subistituir o idDoProfissional por um valor inteiro de um id do profissional.</p>
   
  
 


