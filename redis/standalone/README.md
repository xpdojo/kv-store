# Standalone

```sh
sudo docker-compose up -d
```

```sh
Attaching to redis
redis  | 1:C 14 Aug 2022 12:13:40.105 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
redis  | 1:C 14 Aug 2022 12:13:40.105 # Redis version=5.0.14, bits=64, commit=00000000, modified=0, pid=1, just started
redis  | 1:C 14 Aug 2022 12:13:40.105 # Configuration loaded
redis  |                 _._                                                  
redis  |            _.-``__ ''-._                                             
redis  |       _.-``    `.  `_.  ''-._           Redis 5.0.14 (00000000/0) 64 bit
redis  |   .-`` .-```.  ```\/    _.,_ ''-._                                   
redis  |  (    '      ,       .-`  | `,    )     Running in standalone mode
redis  |  |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
redis  |  |    `-._   `._    /     _.-'    |     PID: 1
redis  |   `-._    `-._  `-./  _.-'    _.-'                                   
redis  |  |`-._`-._    `-.__.-'    _.-'_.-'|                                  
redis  |  |    `-._`-._        _.-'_.-'    |           http://redis.io        
redis  |   `-._    `-._`-.__.-'_.-'    _.-'                                   
redis  |  |`-._`-._    `-.__.-'    _.-'_.-'|                                  
redis  |  |    `-._`-._        _.-'_.-'    |                                  
redis  |   `-._    `-._`-.__.-'_.-'    _.-'                                   
redis  |       `-._    `-.__.-'    _.-'                                       
redis  |           `-._        _.-'                                           
redis  |               `-.__.-'                                               
redis  | 
redis  | 1:M 14 Aug 2022 12:13:40.106 # WARNING: The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis  | 1:M 14 Aug 2022 12:13:40.106 # Server initialized
redis  | 1:M 14 Aug 2022 12:13:40.106 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis  | 1:M 14 Aug 2022 12:13:40.106 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
redis  | 1:M 14 Aug 2022 12:13:40.106 * Ready to accept connections
```
