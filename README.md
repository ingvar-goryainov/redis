# Redis Cluster 

* Build master-slave redis cluster
* Try all eviction strategies
* Write a wrapper for Redis Client that implement probabilistic cache clearing

## Docker output

````
redis-slave           | 1:S 01 Jun 2022 20:07:02.183 * Ready to accept connections
redis-slave           | 1:S 01 Jun 2022 20:07:02.183 * Connecting to MASTER redis-master:6379
redis-slave           | 1:S 01 Jun 2022 20:07:02.185 * MASTER <-> REPLICA sync started
redis-slave           | 1:S 01 Jun 2022 20:07:02.185 * Non blocking connect for SYNC fired the event.
redis-slave           | 1:S 01 Jun 2022 20:07:02.185 * Master replied to PING, replication can continue...
redis-slave           | 1:S 01 Jun 2022 20:07:02.186 * Trying a partial resynchronization (request ae9db327e040f5403a78ef79d9e17bb0609edaf7:7477091).
redis-master          | 1:M 01 Jun 2022 20:07:02.186 * Replica 172.24.0.3:6379 asks for synchronization
redis-master          | 1:M 01 Jun 2022 20:07:02.186 * Partial resynchronization not accepted: Replication ID mismatch (Replica asked for 'ae9db327e040f5403a78ef79d9e17bb0609edaf7', my replication IDs are '339756353f195d468a65adf3dd2be0bd648c5945' and '0000000000000000000000000000000000000000')
redis-master          | 1:M 01 Jun 2022 20:07:02.186 * Replication backlog created, my new replication IDs are 'd9f55374d5ea8619f4ce3ab2354f317f417e0efd' and '0000000000000000000000000000000000000000'
redis-master          | 1:M 01 Jun 2022 20:07:02.186 * Delay next BGSAVE for diskless SYNC
redis-master          | 1:M 01 Jun 2022 20:07:04.100 # Cluster state changed: ok
redis-master          | 1:M 01 Jun 2022 20:07:07.923 * Starting BGSAVE for SYNC with target: replicas sockets
redis-slave           | 1:S 01 Jun 2022 20:07:07.924 * Full resync from master: d9f55374d5ea8619f4ce3ab2354f317f417e0efd:2179
redis-master          | 1:M 01 Jun 2022 20:07:07.924 * Background RDB transfer started by pid 22
redis-slave           | 1:S 01 Jun 2022 20:07:07.926 * MASTER <-> REPLICA sync: receiving streamed RDB from master with EOF to disk
redis-slave           | 1:S 01 Jun 2022 20:07:07.926 * Discarding previously cached master state.
redis-slave           | 1:S 01 Jun 2022 20:07:07.926 * MASTER <-> REPLICA sync: Flushing old data
redis-slave           | 1:S 01 Jun 2022 20:07:07.927 * MASTER <-> REPLICA sync: Loading DB in memory
redis-master          | 22:C 01 Jun 2022 20:07:07.926 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
redis-master          | 1:M 01 Jun 2022 20:07:07.926 # Diskless rdb transfer, done reading from pipe, 1 replicas still up.
redis-slave           | 1:S 01 Jun 2022 20:07:07.929 * Loading RDB produced by version 7.0.0
redis-slave           | 1:S 01 Jun 2022 20:07:07.929 * RDB age 0 seconds
redis-slave           | 1:S 01 Jun 2022 20:07:07.929 * RDB memory usage when created 2.00 Mb
redis-slave           | 1:S 01 Jun 2022 20:07:07.930 * Done loading RDB, keys loaded: 2824, keys expired: 0.
redis-slave           | 1:S 01 Jun 2022 20:07:07.930 * MASTER <-> REPLICA sync: Finished with success
redis-master          | 1:M 01 Jun 2022 20:07:07.930 * Background RDB transfer terminated with success
redis-master          | 1:M 01 Jun 2022 20:07:07.930 * Streamed RDB transfer with replica 172.24.0.3:6379 succeeded (socket). Waiting for REPLCONF ACK from slave to enable streaming
redis-master          | 1:M 01 Jun 2022 20:07:07.930 * Synchronization with replica 172.24.0.3:6379 succeeded
````

## Redis cli `Info` outpit

````
# Replication
role:master
connected_slaves:1
slave0:ip=172.24.0.3,port=6379,state=online,offset=3261863,lag=0
master_failover_state:no-failover
master_replid:d9f55374d5ea8619f4ce3ab2354f317f417e0efd
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:3271213
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:2207521
repl_backlog_histlen:1063693

# CPU
used_cpu_sys:4.300814
used_cpu_user:1.162863
used_cpu_sys_children:0.013486
used_cpu_user_children:0.006375
used_cpu_sys_main_thread:4.258444
used_cpu_user_main_thread:1.157914

# Modules

# Errorstats
errorstat_NOAUTH:count=1

# Cluster
cluster_enabled:1

# Keyspace
db0:keys=2883,expires=2882,avg_ttl=69121
````

## Output when save to rdb file

````
redis-master          | 1:M 01 Jun 2022 20:08:02.054 * 10000 changes in 60 seconds. Saving...
redis-master          | 1:M 01 Jun 2022 20:08:02.055 * Background saving started by pid 23
redis-master          | 23:C 01 Jun 2022 20:08:02.062 * DB saved on disk
redis-master          | 23:C 01 Jun 2022 20:08:02.063 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
redis-master          | 1:M 01 Jun 2022 20:08:02.156 * Background saving terminated with success
redis-slave           | 1:S 01 Jun 2022 20:08:03.061 * 10000 changes in 60 seconds. Saving...
redis-slave           | 1:S 01 Jun 2022 20:08:03.062 * Background saving started by pid 22
redis-slave           | 22:C 01 Jun 2022 20:08:03.067 * DB saved on disk
redis-slave           | 22:C 01 Jun 2022 20:08:03.068 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
redis-slave           | 1:S 01 Jun 2022 20:08:03.163 * Background saving terminated with success
````
