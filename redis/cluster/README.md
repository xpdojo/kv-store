# Cluster

## 실행

```sh
sudo docker-compose up -d
```

```sh
docker exec -it redis-node-1 redis-cli -p 7001 info
```

## 마스터(Master) 노드 클러스터 생성

```sh
# docker exec -it redis-node-1 sh
# redis-cli --cluster create 172.30.0.31:7001 172.30.0.32:7002 172.30.0.33:7003
# docker exec -it redis-node-1 redis-cli --cluster create 172.30.0.31:7001 172.30.0.32:7002 172.30.0.33:7003
```

```sh
# add slave
docker exec -it redis-node-2 redis-cli -p 7002 --cluster add-node 172.30.0.32:7002 172.30.0.31:7001 --cluster-slave

# list slots
docker exec -it redis-node-1 redis-cli -p 7001 cluster slots

# add slots
docker exec -it redis-node-1 redis-cli -p 7001 cluster addslots 10000
```

```sh
>>> Performing hash slots allocation on 3 nodes...
Master[0] -> Slots 0 - 5460
Master[1] -> Slots 5461 - 10922
Master[2] -> Slots 10923 - 16383
M: ee9a897e03f1f641f0317c2e8fd09e488537d4e3 172.30.0.31:7001
   slots:[0-5460] (5461 slots) master
M: 18bebaa483fc328ea81881dbabf52ac55debea43 172.30.0.32:7002
   slots:[5461-10922] (5462 slots) master
M: 575aad00055615c2661370492e89d7c34e50a19d 172.30.0.33:7003
   slots:[10923-16383] (5461 slots) master
Can I set the above configuration? (type 'yes' to accept): yes 
>>> Nodes configuration updated
>>> Assign a different config epoch to each node
>>> Sending CLUSTER MEET messages to join the cluster
Waiting for the cluster to join
.
>>> Performing Cluster Check (using node 172.30.0.31:7001)
M: ee9a897e03f1f641f0317c2e8fd09e488537d4e3 172.30.0.31:7001
   slots:[0-5460] (5461 slots) master
M: 575aad00055615c2661370492e89d7c34e50a19d 172.30.0.33:7003
   slots:[10923-16383] (5461 slots) master
M: 18bebaa483fc328ea81881dbabf52ac55debea43 172.30.0.32:7002
   slots:[5461-10922] (5462 slots) master
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

### 클러스터 상태 확인

먼저 해당 노드를 확인한다.

```sh
redis-cli -c -p 7001 info replication
```

```sh
# Replication
role:master
connected_slaves:0
master_replid:ccbd35230745d651cef783ad8d27410ac629a3e7
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0
```

클러스터로 묶인 노드를 확인한다.

```sh
redis-cli -c -p 7001 cluster nodes
```

```sh
575aad00055615c2661370492e89d7c34e50a19d 172.30.0.33:7003@17003 master - 0 1660484607489 3 connected 10923-16383
18bebaa483fc328ea81881dbabf52ac55debea43 172.30.0.32:7002@17002 master - 0 1660484607489 2 connected 5461-10922
ee9a897e03f1f641f0317c2e8fd09e488537d4e3 172.30.0.31:7001@17001 myself,master - 0 1660484607000 1 connected 0-5460
```

전체 클러스터 정보를 확인한다.

```sh
redis-cli -c -p 7001 cluster info
```

```sh
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:3
cluster_size:3
cluster_current_epoch:3
cluster_my_epoch:1
cluster_stats_messages_ping_sent:229
cluster_stats_messages_pong_sent:243
cluster_stats_messages_sent:472
cluster_stats_messages_ping_received:241
cluster_stats_messages_pong_received:229
cluster_stats_messages_meet_received:2
cluster_stats_messages_received:472
```

## 복제(Replica, Slave) 노드 추가

- [Redis replication](https://redis.io/docs/manual/replication/)

```sh
```

## 센티널(Sentinel) 노드 추가

- [High availability with Redis Sentinel](https://redis.io/docs/manual/sentinel/)

```sh
```

## Snapshot

- [Redis persistence](https://redis.io/docs/manual/persistence/)

```redis.conf
save 60 1000
```
