#! venv/bin/python3
import yaml
import json
import argparse
# import doctest

def validate_pod(pod: dict, prefix: str, port_range: tuple[int]) -> bool:
    '''
    validate_pod: iterates the containers in a given pod spec, and validates 
    (a) the container image is from an allowed registry identified by PREFIX
    (b) all container ports lie within the range bounded by port_range[0] and port_range[1]
    >>> validate_pod(dict(spec=dict(containers=[dict(image="my-registry.io/apache")])), "my-registry.io/", (5000, 1000))
    True
    '''
    valid = True
    results = {"validation results": []} 
    with open("status_report.json", 'w') as outfile:
        for container in pod["spec"]["containers"]:
            if not container.get("image", "").startswith(prefix):
                valid = False
                results['validation results'].append({f'{container.get("name")} image validation': {'status': 'failed', 'reason': f'image {container.get("image")} not from expected registry: {prefix}'}}) # add the validation result and reason to outputs
            else:
                results['validation results'].append({f'{container.get("name")} image validation': {'status': 'passed', 'reason': f'image {container.get("image")} from expected registry: {prefix}'}})
            for port in container.get("ports", dict()):
                if not (port_range[0] <= port.get("containerPort", 0) <= port_range[1]):
                    valid = False
                    results['validation results'].append({f'{container.get("name")} port validation': {'status': 'failed', 'reason': f'port {port.get("containerPort")} not in range {port_range[0]} - {port_range[1]}'}})
                else:
                    results['validation results'].append({f'{container.get("name")} port validation': {'status': 'passed', 'reason': f'port {port.get("containerPort")} in required range {port_range[0]} - {port_range[1]}'}})
        json.dump(results, outfile, indent=2)
        return valid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    parser.add_argument("--prefix")
    parser.add_argument("--port-min", type=int)
    parser.add_argument("--port-max", type=int)
    args = parser.parse_args()
    with open(args.file, 'r') as podfile:
        input_yaml = yaml.safe_load(podfile)
        pod = input_yaml if input_yaml["kind"] == "Pod" else input_yaml["spec"]["template"] # stretch goal 3
        validation = validate_pod(pod, prefix=args.prefix, port_range=(args.port_min, args.port_max))
        if validation:
            print("all validations passed")
        else:
            print("validation failed - see status_report.json for details")