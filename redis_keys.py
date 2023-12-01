import redis

# Connect to Redis
r = redis.Redis(host="localhost", port=6379, db=0)

print("Connected to Redis")

# Get all keys
keys = r.keys()

print(f"Found {len(keys)} keys in the database")

# Print each key
for key in keys:
    type = r.type(key).decode()
    key = key.decode()
    print(f"Key: {key}, Type: {type}")

    if type == "string":
        value = r.get(key).decode()
        print(f"Value: {value}")
    elif type == "list":
        value = [item.decode() for item in r.lrange(key, 0, -1)]
        print(f"Value: {value}")
    elif type == "set":
        value = {item.decode() for item in r.smembers(key)}
        print(f"Value: {value}")
    elif type == "hash":
        value = {k.decode(): v.decode() for k, v in r.hgetall(key).items()}
        print(f"Value: {value}")
    else:
        print("Unsupported type")
