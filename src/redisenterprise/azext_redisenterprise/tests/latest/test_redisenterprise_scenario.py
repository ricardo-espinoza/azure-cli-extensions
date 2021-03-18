# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_create
from .example_steps import step_show
from .example_steps import step_list
from .example_steps import step_list2
from .example_steps import step_database_show
from .example_steps import step_database_list
from .example_steps import step_database_list_keys
from .example_steps import step_database_regenerate_key
from .example_steps import step_delete
from .example_steps import step_database_create
from .example_steps import step_database_delete
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario1
@try_manual
def setup_scenario1(test, rg):
    pass


# Env cleanup_scenario1
@try_manual
def cleanup_scenario1(test, rg):
    pass


# Testcase: scenario1
@try_manual
def call_scenario1(test, rg):
    setup_scenario1(test, rg)
    step_create(test, rg, checks=[])
    step_show(test, rg, checks=[])
    step_list(test, rg, checks=[])
    step_list2(test, rg, checks=[])
    step_database_show(test, rg, checks=[])
    step_database_list(test, rg, checks=[])
    step_database_list_keys(test, rg, checks=[])
    step_database_regenerate_key(test, rg, checks=[])
    step_delete(test, rg, checks=[])
    cleanup_scenario1(test, rg)


# Test class for scenario1
@try_manual
class Redisenterprisescenario1Test(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(Redisenterprisescenario1Test, self).__init__(*args, **kwargs)

    @ResourceGroupPreparer(name_prefix='clitestredisenterprise_rg1'[:7], key='rg', parameter_name='rg')
    def test_redisenterprise_scenario1(self, rg):
        call_scenario1(self, rg)
        calc_coverage(__file__)
        raise_if()


# Env setup_scenario2
@try_manual
def setup_scenario2(test, rg):
    pass


# Env cleanup_scenario2
@try_manual
def cleanup_scenario2(test, rg):
    pass


# Testcase: scenario2
@try_manual
def call_scenario2(test, rg):
    setup_scenario2(test, rg)
    step_create(test, rg, checks=[])
    step_show(test, rg, checks=[])
    step_list(test, rg, checks=[])
    step_list2(test, rg, checks=[])
    step_database_create(test, rg, checks=[])
    step_database_show(test, rg, checks=[])
    step_database_list(test, rg, checks=[])
    step_database_list_keys(test, rg, checks=[])
    step_database_regenerate_key(test, rg, checks=[])
    step_database_delete(test, rg, checks=[])
    step_delete(test, rg, checks=[])
    cleanup_scenario2(test, rg)


# Test class for scenario2
@try_manual
class Redisenterprisescenario2Test(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(Redisenterprisescenario2Test, self).__init__(*args, **kwargs)

    @ResourceGroupPreparer(name_prefix='clitestredisenterprise_rg1'[:7], key='rg', parameter_name='rg')
    def test_redisenterprise_scenario2(self, rg):
        call_scenario2(self, rg)
        calc_coverage(__file__)
        raise_if()
