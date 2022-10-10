# redis-cli

- [redis-cli](#redis-cli)
  - [System Commands](#system-commands)
    - [연결 상태 확인](#연결-상태-확인)
  - [CRUD Commands](#crud-commands)
    - [모든 Key 조회 - KEYS](#모든-key-조회---keys)
    - [모든 key 조회 - SCAN](#모든-key-조회---scan)
    - [get](#get)
    - [저장된 key 개수 조회](#저장된-key-개수-조회)
    - [type](#type)
  - [참조](#참조)

## System Commands

### 연결 상태 확인

```sh
ping
# PONG
```

## CRUD Commands

### 모든 Key 조회 - KEYS

운영에서는 사용하지 않는다.
O(N) 명령어는 모든 키를 스캔하므로, 키가 많은 경우에는 매우 느려져서
Redis에 의존하고 있는 서버를 멈추게 만들 수 있다.

```sh
keys *
#  1) "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:markruler"
#  2) "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:tester"
#  3) "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:david"
#  4) "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:john"
#  5) "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:hey"
```

```sh
keys *mark*
#  1) "spring:session:index:org.springframework.session.FindByIndexNameSessionRepository.PRINCIPAL_NAME_INDEX_NAME:markruler"
```

### 모든 key 조회 - SCAN

```sh
scan 0
# 1) "17"
# 2)  1) "key:12"
#     2) "key:8"
#     3) "key:4"
#     4) "key:14"
#     5) "key:16"
#     6) "key:17"
#     7) "key:15"
#     8) "key:10"
#     9) "key:3"
#    10) "key:7"
#    11) "key:1"

scan 17
# 1) "0"
# 2) 1) "key:5"
#    2) "key:18"
#    3) "key:0"
#    4) "key:2"
#    5) "key:19"
#    6) "key:13"
#    7) "key:6"
#    8) "key:9"
#    9) "key:11"
```

### get

```sh
get ${key}
```

### 저장된 key 개수 조회

```sh
dbsize
```

```sh
info keyspace
```

### type

```sh
type ${key}
```

## 참조

- [Redis Documentation](https://redis.io/documentation)
- [레디스게이트 (RedisGate)](http://redisgate.kr/redis/command/commands.php)
