# Social-network (Technical Task)

## Dependencies

- [poetry](https://python-poetry.org/docs/#installing-manually)
- [docker](https://docs.docker.com/get-docker/)

### requirements.txt (run before build images)

```shell
 poetry export -f requirements.txt --output requirements.txt --without-hashes
```

### Build

```shell
docker-compose -f .\docker\compose\docker-compose.local.yml -p sn build

# or
docker build -f .\docker\django\Dockerfile -t sn-app:dev .
docker build -f .\docker\notebook\Dockerfile -t sn-notebook:dev .  # need for testing bot

# or
make build
```

### Start 

```shell
docker-compose -f .\docker\compose\docker-compose.local.yml -p sn up -d

# or
make up
```

### BOT
For testing bot script you need: 
- fill in the environment variables in the `/docker/environment/bot.local.env` file before running the containers
- open `bot.ipynb` in jupyter notebook and run all cells


### Note
After starting the containers, 
it'll create default superuser with such credentials:
- login `super-admin@example.com`  
- password `super-admin123`