from benchmark import Benchmark


class AnyBool(Benchmark):
    def inner_benchmark_loop(self, inner_iterations):
        sum_ = 0

        for i in range(inner_iterations):
            sum_ += 1 if any([False] * i) else 0

        return sum_ == 0

    def benchmark(self):
        raise Exception("Should never be reached")

    def verify_result(self, result):
        raise Exception("Should never be reached")
