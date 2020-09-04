def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create hash table
    cache = {}
    # set up array
    result = []
    # set count to zero
    count = 0

    # checking if item is in arrays
    for item in arrays:
        # looping through
        for lists in item:
            if lists not in cache:
                cache[lists] = 1
            else:
                cache[lists] += 1 
        count += 1

    # for loop passing key, value pairs into cache
    for k, v in cache.items():
        # set up - if value is greater than 1
        if v > 1:
            result.append(k)

    # return result of intersections
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
