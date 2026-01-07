from py04_soln import validate_pod

invalid_sample_spec = dict(spec=dict(containers=[dict(image="docker.io/apache")]))
valid_sample_spec = dict(spec=dict(containers=[dict(image="my-registry.io/apache")]))

def test_valid_pod():
    valid = validate_pod(valid_sample_spec, "my-registry.io/", (5000, 10000))
    assert valid

def test_invalid_pod():
    valid = validate_pod(invalid_sample_spec, "my-registry.io/", (5000, 10000))
    assert not valid