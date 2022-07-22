import random

probabilities = [0.1, 0.2, 0.4, 0.2, 0.1]


def samples_simulate(args, samples_count, simulate_count, offset):
    """

    Args:
        args: probabilities[]
        samples_count: The number of generated samples
        simulate_count: Number of times to simulate random sampling
        offset: if you want get [1,2,3,4] offset is 1; [2,3,4] offset is 2 ......

    Returns: simulated data

    """
    # Save samples generated from probability distributions
    samples = []
    # Save the number of times each data category was selected For example, samples_choosed[0]=10 indicates that data
    # category 0 was selected 10 times during a large number of random sampling
    samples_choosed = {}
    # probabilities calculated from a large number of random samples
    test_probabilities = {}

    # Iterate (data category, probability) pairs
    for index, pro in enumerate(args):
        # Generate a corresponding number of samples according to the probability
        for i in range(round(pro * samples_count)):
            samples.append(index + offset)
        samples_choosed[index + offset] = 0
        test_probabilities[index + offset] = 0.0
    # Shuffle the order of samples by re-shuffling the list
    random.shuffle(samples)
    print('length of samples is: ', samples.__len__())
    # Perform random sampling of simulate_count times and record the number of times each data category is sampled
    for i in range(simulate_count):
        index = int(random.random() * samples_count)
        try:
            samples_choosed[samples[index]] += 1
        except Exception as e:
            continue

    # Calculate how often each data class is sampled
    for (index, count) in samples_choosed.items():
        test_probabilities[index] = count / float(simulate_count)

    # print simulated data
    print(samples)
    # print probability of the simulated data
    print(test_probabilities)

    return samples


# samples_simulate(probabilities, 13, 10000, 1)
