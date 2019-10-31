# Valida CPF

Para executar a API:

`$ git clone https://gitlab.com/gcc129/valida-cpf.git`

`$ cd valida-cpf`

`$ npm install`

`$ npm start`

Para testar em localhost:

`$ curl localhost:5000/`

`$ curl localhost:5000/validar/12345678900`

# Trabalho
- ...criando a imagem
`docker build -t nodeserver:001 .`

- ...criando os container a partir das imagens criadas
`docker container run -p 5001:5000 --name customized1 -e "name=container001" -d nodeserver:001`
`docker container run -p 5002:5000 --name customized2 -e "name=container002" -d nodeserver:001`
`docker container run -p 5003:5000 --name customized3 -e "name=container003" -d nodeserver:001`

- ...criando balanceamento de carga
`cd balance`
`docker build -t nginxbalancer:001 .`
`docker container run -p 5000:80 -d nginxbalancer:001`