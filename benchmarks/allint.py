from benchmark import Benchmark


class AllInt(Benchmark):
    def inner_benchmark_loop(self, inner_iterations):
        sum_ = 0

        for i in range(inner_iterations):
            sum_ += 1 if all([1] * i) else 0

        return sum_ == inner_iterations

    def benchmark(self):
        raise Exception("Should never be reached")

    def verify_result(self, result):
        raise Exception("Should never be reached")
