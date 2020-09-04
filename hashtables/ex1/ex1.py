def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create an empty dictionary
    cache = {}

    # set up for loop
    for weight in range(len(weights)):
        # setting the higher(current)
        higher = weights[weight]

        # checking if the higher weight is in the cache
        if higher in cache:
            # setting the lower(previous) variable, and passing in the higher value in the cache
            lower = cache[higher]
            print(cache[weights[weight]])

            # The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index order
            return (weight, lower) 

        # printing the entire cache
        print('Weights:', cache)

        # If we store each weight's list index as its value, we can then check to see if the hash table contains an entry for `limit - weight`. If it does, then we've found the two items whose weights sum up to the `limit`!
        cache[limit - higher] = weight

    return None
