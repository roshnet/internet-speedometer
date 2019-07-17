
def use_mean(d):
    """
    :param d:       A dictionary with keys and values as float/int.

    Returns:        (mean of keys) / (mean of values)

    """
    mean_k = sum(d.keys()) / len(d.keys())
    mean_v = sum(d.values()) / len(d.values())
    return  mean_k / mean_v


def use_sum(d):
    """
    :param d:       A dictionary with keys and values as float/int.

    Returns:        (sum of keys) / (sum of values)

    """
    sum_k = sum(d.keys())
    sum_v = sum(d.values())
    return sum_k / sum_v


def paired_mean(d):
    """
    :param d:       A dictionary with keys and values as float/int.

    Returns:        Mean of results from each pair.

    """
    keys = d.keys()
    values = d.values()
    means = []
    for i in range(len(d)):
        means.append(keys[i] / values[i])
    
    mean = sum(means) / len(means)
    return mean
