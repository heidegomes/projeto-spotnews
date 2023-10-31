# :construction: README em construção ! :construction:
<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->

<details>
1. Este projeto usa dependências que não são funcionais em todas as versões do Python. Por isso, recomendamos que seu Python esteja na versão `3.10.0` ou superior. Você pode usar o `Pyenv`, basta seguir nosso tutorial sobre [instalação e uso do Pyenv](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/f04cdb21-382e-4588-8950-3b1a29afd2dd/section/aa76abc8-b842-40d9-b5cc-baa960952129/lesson/0fe67ea0-1046-4b55-a37c-44afcfa9ed0a).
  
> ⚠️ **ATENÇÃO: NUNCA REMOVA VERSÕES ANTIGAS INSTALADAS DO PYTHON. SEU SISTEMA OPERACIONAL PODE DEPENDER DELAS!** ⚠️

2. Para conseguir instalar a dependência `mysqlclient` você precisa garantir a existência de algumas bibliotecas no seu sistema operacional:

- **Debian/Ubuntu**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

- **Mac**
```bash
brew install mysql pkg-config
```
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>


python3 manage.py runserver
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runscript seeds
