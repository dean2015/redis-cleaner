from rediscluster import StrictRedisCluster
import sys

class RedisProcess(object):
    cluster_nodes = []
    redisconn = None

    def __init__(self, cluster_nodes):
        self.cluster_nodes = cluster_nodes
        self.connect()

    def connect(self):
        try:
            self.redisconn = StrictRedisCluster(startup_nodes=self.cluster_nodes)
        except Exception as e:
            print("Connect Error!")
            sys.exit(1)

    def clear(self, pattern):
        print('Clean keys with pattern: ' + pattern)
        print('started')
        if self.redisconn:
            for key in self.redisconn.keys(pattern):
                self.redisconn.delete(key)
                print(str(key) + ' removed')
