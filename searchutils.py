import numpy as np

def neighbors_func(state):
    """
    Creates all neighbors of a given state
    A state's neighbor is identical to the state except at exactly one
    position

    :param state: binary array describing used PSUs
    :return: 2D array containing all state's neighbors
    """
    neighbors = np.tile(state, (state.size, 1))
    diagonal = np.diagonal(neighbors)

    for i in range(state.size):
        neighbors[i, i] = not diagonal[i]

    return neighbors

def value_function(state, order, psus):
    """
    Evaluates how good a subset of PSU fulfills the order

    :param state: binary array describing used PSUs
    :param order: binary representation of current order
    :param psus: 2d array containing binary representation of all psus
    :return: value of state
    """
    # a list of the psus (including its items) used in the state
    psus_in_state = np.compress(state, psus, axis=0)

    # CALCULATE VALUES
    # if the state is empty
    if len(psus_in_state) == 0:
        return -10 * (np.size(state))
    # else count the missing elements
    items = np.bitwise_or.reduce(psus_in_state, 0)

    # if all elements are covered, minimize the amount of used psus
    if np.all(items):
        return np.count_nonzero(state == False)
    # else elements are missing
    else:
        return -1 * (np.size(items) - np.count_nonzero(items))
