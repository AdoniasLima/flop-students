## Desenvolvimento de aplicativo 

Preparando pastas para o desenvolvimento  
  
- 14/03/2019 - Autor: Adonias, Descrição: Adicionando os arquivos do curso na pasta proposta-2, todos os diretórios estão declarados no .gitignore;

- Tutorial para clonagem do arquivo e para contribuição no repositório, tanto no perfil do contribuidor como no perfil principal.

- Primeiro passo: após instalar o git, vamos fazer o clone da aplicação:[

    git clone https://github.com/AdoniasLima/flop-students.git
    
- Segundo passo: acesse a pasta flop-students

    cd flop-students
    
- Terceiro passo: definir um novo remoto apontando para o projeto principal. 

    git remote add upstream https://github.com/AdoniasLima/flop-students.git
    
- Quarto passo: OBS: Antes de criar ou alterar qualquer coisa crie uma branch para as alterações que você vai fazer.

    git checkout -b adonias 
    
    // O comando "git checkout" troca a branch e o "-b" cria a branch, os comandos separados ficariam dessa forma:
    // "git branch adonias" cria a branch mas não troca automaticamente.
    // "git checkout adonias" troca para a branch
  
- Comandos para resgatar as últimas atualizações e fazer o upload dos seus arquivos.
  
    git pull origin master //Este comando resgata as últimas alterações do da branch master. Obs: a branch master apenas quando o projeto for finalizado.
    
    git push origin seuabranch //Este comando envia para o seu repositório e para o orginal as alterações na sua branch. 
