import pytest
import pickle
from .all_modules import all_environments
from .api_test import api_test
from .seed_test import seed_test
from .parallel_test import parallel_play_test
from .max_cycles_test import max_cycles_test
import os


@pytest.mark.parametrize(("name", "env_module"), list(all_environments.items()))
def test_module(name, env_module):
    _env = env_module.env()
    assert str(_env) == os.path.basename(name)
    api_test(_env)
    if "classic/" not in name:
        parallel_play_test(env_module.parallel_env())

    if "prospector" not in name:
        seed_test(env_module.env, 50)

    if "classic/" not in name:
        max_cycles_test(env_module)

    recreated_env = pickle.loads(pickle.dumps(_env))
    api_test(recreated_env)
