## IEFP_Flask

Projeto em **Flask** com **Base de Dados MariaDB/MySQL**

### Dependencias

Podem ser instadas com recurso ao ficheiro ```requirements.txt``` através do comando
````commandline
pip install -r requirements.txt
````

###### Nota: para instalar a dependencias terão que correr o comando na directoria principal.

### Criação de Ambiente virtual

Para criar o nosso ambiente virtual, basta correr o seguinte comando:

`````commandline
python -m venv venv
`````

### Estrutura do Projecto

```shell
  ├── README.md
  ├── app.py *** ficheiro python principal
  ├── requirements.txt *** ficheiro de dependencias "pip install -r requirements.txt"
  ├── static
  │   ├── css *** ficheiros css
  └── templates *** ficheiros html
  ```

### Base de Dados

Teremos que criar uma base de dados chamada ``empresa`` e inserir alguns dados através do ficheiro ``empresa.sql``.

Temos que ligar-nos à nossa instância de MariaDB/MySQL:
````commandline
mariadb -u UTILIZADOR -p
````

Depois podemos fazer outsource do nosso script sql:
````mysql
source sql\empresa.sql
````
###### NOTA: o comando acima assume que estamos no diretório principal

Com isto, estamos prontos para lançar a nossa aplicação.

### Lançar o nosso servidor de desenvolvimento

Aconselho a criação de um ficheiro ``.env`` e colocar as seguintes linhas:

````commandline
FLASK_APP=app.py
FLASK_ENV=development
````

Depois podemos lançar a aplicação dentro do nosso ambiente virtual:

````commandline
flask run
````