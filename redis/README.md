# Redis

## Quick Start

```sh
sudo docker run \
  --name=redis-local \
  --detach \
  --restart=always \
  --publish 6379:6379 \
  redis:5.0.13
```

## CLI Usage

```sh
# redis-cli -p 6379
sudo docker exec -it redis-local redis-cli
```

```sh
help
```
