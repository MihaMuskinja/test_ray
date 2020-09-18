#!/usr/bin/env python
"""
A simple test of Ray
"""

import argparse
import os
import ray
import time


@ray.remote
def ping():
    time.sleep(0.01)
    return os.getpid()


def main(args):
    ray.init(num_cpus=int(args.num_processes))

    pids = []
    for _ in range(1000):
        pids += [ping.remote()]

    unique_pids = set(ray.get(pids))
    print(f"number of unique processes spawned: {len(unique_pids)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='test ray')
    parser.add_argument('-n', '--num-processes')
    args = parser.parse_args()

    assert args.num_processes
    main(args)
