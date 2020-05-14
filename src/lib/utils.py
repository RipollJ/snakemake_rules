# Author: JR & FC
# Created: 2020-05-14
# License: MIT


# Import for snakemake
from snakemake.utils import update_config
from snakemake.io import Params

# Class for set params
class StubParams(Params):
    def __init__(self, prefix):
        self.__prefix__ = prefix if prefix else ""

    def __getattribute__(self, key):
        if key.startswith('__'):
            return super().__getattribute__(key)
        else:
            return "{"+self.__prefix__+"."+key+"}"

    def __str__(self):
        return "{"+self.__prefix__+"}"

# Catch vars
STUB_SNAKEMAKE_VARS = {
    "input": StubParams("input"),
    "log": StubParams("log"),
    "output": StubParams("output"),
    "params": StubParams("params"),
    "resources": StubParams("resources"),
    "rule": StubParams("rule"),
    "threads": StubParams("threads"),
    "wildcards": StubParams("wildcards")
}

# Function to inject vars
def inject(fn, snakemake_vars):
    if 'rule' in snakemake_vars:
        return fn(**snakemake_vars)
    else:
        return "WARNING : snakemake values are not currently available, can result in inconsistencies in the displayed shell command.\n"+fn(**STUB_SNAKEMAKE_VARS)

# Function for merging default params and customized params
def merge_dict(default, overwrite):
    if isinstance(overwrite, StubParams):
        return Params(fromdict=default)

    config = {}
    update_config(config, default)
    update_config(config, overwrite)
    return Params(fromdict=config)

# Function for merging args
def merge_strings(*args, join_string=" "):
    return join_string.join(filter(None, args))
    
####
# END

