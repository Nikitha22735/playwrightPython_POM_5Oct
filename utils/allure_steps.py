from contextlib import contextmanager
from typing import Iterator

import allure


@contextmanager
def test_step(name: str) -> Iterator[None]:
    with allure.step(name):
        yield
