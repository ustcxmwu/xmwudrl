import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


@pytest.fixture(scope="session")
def root_path():
    print(Path(__file__).parents)
    return Path(__file__).parents[1]

