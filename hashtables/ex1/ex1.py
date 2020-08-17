def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}
    for i in range(length): 
        value = weight_dict.get(limit-weights[i])
        if value is not None:
            return (i, value)
        else:
            weight_dict[weights[i]] = i
    print(weight_dict)

    return None
