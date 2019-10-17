from femos.core import get_number_of_nn_weights, get_random_numbers


def test_get_random_numbers():
    quantity = 500
    lower_threshold = -1
    upper_threshold = 1

    random_numbers = get_random_numbers(quantity, lower_threshold, upper_threshold)
    assert len(random_numbers) == quantity

    for element in random_numbers:
        assert lower_threshold <= element <= upper_threshold


def test_get_number_of_nn_weights():
    assert get_number_of_nn_weights(9, [4, 4], 9) == 88
    assert get_number_of_nn_weights(9, [], 9) == 81
    assert get_number_of_nn_weights(9, [8, 8, 8], 1) == 208
