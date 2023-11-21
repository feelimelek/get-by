Para inicializar esse container separadamente no momento de desenvolvimento:

sudo  docker run --name pg-container-name -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -v /path/to/init.sql:/docker-entrypoint-initdb.d/init.sql -d postgres 

sudo docker start  d5b343c4f3a88d7dd84fe165f913950a440eb50f1402123515a456694
d66bc31

Para ver se o container do postgres foi inicializado
sudo docker ps

