from recursive_sum2 import rec_sum


def test_rec_sum_gauss_pairing():
    assert rec_sum(1, 5) == 15


def test_rec_sum_pointers_met():
    assert rec_sum(4, 4) == 4
