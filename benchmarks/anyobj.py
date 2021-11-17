from benchmark import Benchmark


class FalseObj:
    def __bool__(self):
        return False


class AnyObj(Benchmark):
    def inner_benchmark_loop(self, inner_iterations):
        sum_ = 0

        for i in range(inner_iterations):
            sum_ += 1 if any([FalseObj()] * i) else 0

        return sum_ == 0

    def benchmark(self):
        raise Exception("Should never be reached")

    def verify_result(self, result):
        raise Exception("Should never be reached")
