# EXPERIMENTAL: all may be removed soon

import numpy as np

from gym.benchmarks import scoring
from gym.benchmarks.registration import register_benchmark, benchmark_spec

register_benchmark(
    id='Atari7Pixel-v0',
    scorer=scoring.ClipTo01ThenAverage(),
    task_groups={
        'BeamRider-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Breakout-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Enduro-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Pong-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Qbert-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Seaquest-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'SpaceInvaders-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
    })

register_benchmark(
    id='Atari7Ram-v0',
    scorer=scoring.ClipTo01ThenAverage(),
    task_groups={
        'BeamRider-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Breakout-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Enduro-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Pong-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Qbert-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'Seaquest-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
        'SpaceInvaders-ram-v0': [{
            'seeds': 1,
            'timesteps': 10000000
        }],
    })