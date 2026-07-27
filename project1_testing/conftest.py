import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--modelN007",
        action="store_true",
        default=False,
        help="Include modelN007 tests in test run",
    )

def pytest_collection_modifyitems(items, config):
    """Deselect tests marked as modelN007 if --modelN007 is set."""  # so mark tests with modelN007 for it to work

    if config.option.modelN007 is True:
        return

    selected_items = []
    deselected_items = []

    for item in items:  #all filtering should be nested 'if-else(elif)'s here
        if item.get_closest_marker("modelN007"):
            deselected_items.append(item)
        else:
            selected_items.append(item)

    config.hook.pytest_deselected(items=deselected_items)
    items[:] = selected_items  #Slicing assignment (and not changing object aka not changing identity)

# not done
@pytest.fixture  #default scope is function
def list_true_false():
    return [True, False]