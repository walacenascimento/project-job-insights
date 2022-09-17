from src.counter import count_ocurrences


def test_counter():
    count_py = count_ocurrences('src/jobs.csv', 'Python')
    count_js = count_ocurrences('src/jobs.csv', 'Javascript')
    assert count_py == 1639
    assert count_js == 122

    # pass
