import importlib.util
import pathlib


def _load_clean():
    root = pathlib.Path(__file__).parent.parent
    spec = importlib.util.spec_from_file_location("clean", root / "clean.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_clean_imports_without_error():
    mod = _load_clean()
    assert mod is not None


def test_clean_add():
    mod = _load_clean()
    assert mod.add(2, 3) == 5


def test_clean_greet():
    mod = _load_clean()
    assert mod.greet("world") == "Hello, world"
