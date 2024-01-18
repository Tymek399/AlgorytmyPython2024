def test_fib():
    assert callable(fib)
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(39) == 63245986

if __name__ == '__main__':
    test_fib()
