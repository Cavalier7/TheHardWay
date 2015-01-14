def new(num_buckets = 256):  # creates a new function with a default argument of 256, also known as an initializer
    """Initializes a Map with the given number of buckets."""
    aMap = [] # creates aMap, a new list
    for i in range(0, num_buckets): # iterates through 0 to 256
        aMap.append([]) # adds a new list inside aMap
    return aMap # returns aMap, now full of lists

def hash_key(aMap, key): # creates function with two arguments
    """Given a key this will create a number and then convert it to an index for the aMap's buckets."""
    return hash(key) % len(aMap) # returns an integer between 0 and 255
    
def get_bucket(aMap, key): # creates functions that takes two arguments
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key) # imports returned bucket from hash_key()
    return aMap[bucket_id] # returns specific bucket where a key might be found

def get_slot(aMap, key, default=None) # new function that accepts three arguments
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set), when not found.
    """
    bucket = get_bucket(aMap, key) # imports aMap[key] from get_bucket()
    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key = k:
            return i, k, v
    
    return -1, key, default

def get(aMap, key, default=None): # new function that accepts three arguments
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default) # gets tuple from get_slot()
    return v # returns either the value or None

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key) 
    i, k, v = get_slot(aMap, key)
    
    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else: # if the key does not exist, get_slot will return i = -1
        # the key does not exist, append to create it
        bucket.append((key, value)) # adds the key, value tuple to the bucket

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
    
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key = k:
            del bucket[i]
            break
        
del list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v
