# Projeto-Horario-Escolar

### Descrição
Proposta de um sistema que controle os horários de entrada e saída escolares, notificando alunos e responsáveis caso ocorram eventuais mudanças. Também incluso um sistema que vai supervisionar a autenticação da chamada presencial do aluno e notificar caso haja divergência entre as agendas.

### 📌 Tarefas

- [ ] Criar o banco de dados com sistema de login para administrador.
- [ ] Adicionar função de agrupamento de dados para que o administrador gerencie turmas, alunos e professores.
- [ ] Criar um sistema que possa definir e alterar o horário de entrada e saída dos alunos.
- [ ] Implementar função de alerta a um bot para sinalizar mudanças no horário.
- [ ] Integrar chamada geral que mostre se o aluno está: presente, ausente ou em ausência justificada.
- [ ] Integrar chamada individual de cada disciplina com as mesmas características da chamada geral.
- [ ] Criar função que observe se há divergências entre as chamadas, e implementar ao bot para que gere o alerta.
- [ ] Revisar possíveis falhas no sistema que possibilitem vazamento de dados importantes.
- [ ] Implementar ao site configurações de responsividade para que se adeque a todos os dispositivos.

### 💡 Ideias e Sugestões

- Criar uma funcionalidade para que professores possam declarar automaticamente sua própria ausência, ou agenda-la.
- Vincular ao "perfil" do aluno o número de celular e email de até dois responsáveis, que só possa ser alterado pelo administrador.
- Criar uma função que permita o administrador declarar e agendar ponto facultativo.
- Possivelmente não utilizar um bot para os alertas e implementar uma área com essa função dentro do sistema

## ⚠ Observações sobre o sistema

- Fazer o programa verificar se há divergência na chamada toda vez que o professor atualizar a situação do aluno no diário.
- Permitir o acesso a grade de horários a qualquer visitante, mesmo que não tenha login.

## 📚 Referências
 [Mindmap](https://www.mindomo.com/mindmap/controle-de-horrio-de-alunos-8dd28347c994422080ea4f7d6e42256e) - Mapa-mental com as principais funcionalidades do projeto.
