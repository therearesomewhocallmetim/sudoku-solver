import importlib
from pathlib import Path


def _module_name(module):
    return module.__name__.split('.')[-1]


def _module_title(module):
    return _module_name(module).replace("_", " ").title()


def _module_doc(module):
    return module.__doc__


def load_strategies(names):
    strategies_dir = Path('commands', 'strategies')
    py_files = [x for x in strategies_dir.iterdir() if x.is_file() and x.name != "__init__.py"]

    modules = [
        importlib.import_module(f"commands.strategies.{py_file.stem}")
        for py_file in py_files]

    all_strategies = [
        (
            _module_name(m),
            _module_title(m),
            _module_doc(m),
            getattr(m, "filter_candidates")
        )
        for m in modules if hasattr(m, "filter_candidates")]
    strategies_by_name = {
        s[0]: s for s in all_strategies
    }

    return [strategies_by_name[name] for name in names]


def load_restrictions(names):
    functions = []
    for module_name, function_name in map(lambda x: x.split('.'), names):
        module = importlib.import_module(f'restrictions.{module_name}')
        try:
            functions.extend(getattr(module, function_name).__call__())
        except AttributeError as e:
            raise AttributeError(
                f"Cannot load restriction {module_name}.{function_name}"
            ) from e
    return functions
