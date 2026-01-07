import timeit

def test_benchmark_validation():
    results = timeit.repeat('py04.validate_pod(dict(spec=dict(containers=[dict(image="my-registry.io/apache")])), "my-registry.io/", (5000, 10000))',
                           setup="import py04_soln as py04", repeat=10, number=10)
    return sum(results) / 100

if __name__ == '__main__':
    print(f"Avg time: {test_benchmark_validation():.2f} seconds")