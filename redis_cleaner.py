from redis_processor import RedisProcess
import sys
import json

redis_nodes = []

with open('config.json', 'r') as f:
    config = json.load(f)
    redis_nodes = config["nodes"]

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        print("Input parameters are not valid.")
        sys.exit(1)
    rp = RedisProcess(redis_nodes)
    rp.clear(argv[1])
    print('done!')
