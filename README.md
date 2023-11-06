# API-com-Django-Rest-Framework

<h4>Frameworks:</h4>
<ul>
  <li>Django</li>
  <li>Django Rest Framework</li>
</ul>
<h4>Bibliotecas:</h4>
 <ul>
    <li>uuid</li>
    <li>validate_docbr</li>
    <li>re</li>
 </ul>
 <h4>Rotas</h4>
   <p><strong>Verbo POST</strong> <br>
   http://127.0.0.1:8000/pessoa-profissional/ - rota para cadastrar uma nova Pessoa Profissional. Campos cpf, possue validação através da biblioteca validate-docbr, com isso é necessário passar um cpf válido para cadastrar a pessoa profissional, bem como o celular também possue validação sendo necessário um celular como este: 11 88855-4444.</p>
  
    {
      "nome": "diogo",
      "nome_social": "diogo-teste",
      "cpf": "123456789",
      "celular": "45 99999-55511",
      "especialidade": "medico",
      "idade": 23,
      "data_nascimento": "1990-05-06"
    }
  
 


