from logging import config

import pytest  # type: ignore[import-not-found]

def pytest_addoption(parser):
    parser.addoption(
        "--modelChoice",
        action="store",
        default="all",
        choices=["all", "model1", "model2"],
        help="specify the model to test. default when specified: model1",
    )

#before the hook runs, pytest should've verified the coice is valid.
def pytest_collection_modifyitems(items, config):
    """this is a demo for using command-line user input to filter tests.
    The user can specify a model to test using the --modelChoice option.
    If the user specifies a model, only tests marked with that model will be run."""

    modelChoice = config.getoption("--modelChoice")
    if(modelChoice == "all"):
        return  #no filtering needed

    selected_items = []
    deselected_items = []

    for item in items:  #all filtering should be nested 'if-else(elif)'s here
        if item.get_closest_marker(modelChoice):
            selected_items.append(item)
        else:
            deselected_items.append(item)
    
    config.hook.pytest_deselected(items=deselected_items) #helps with explicit report of deselection
    items[:] = selected_items  #Slicing assignment (and not changing object aka not changing identity)

# not done
@pytest.fixture  #default scope is function
def list_true_false():
    return [True, False]