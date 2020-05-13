# Author: JR & FC
# Created: 2020-05-12
# License: MIT

# Import for snakemake
from snakemake.utils import update_config
from snakemake.shell import shell

# define default params
DEFAULT_PARAMS = {"one": "one", "two": "two"}

# merge configuration to choose default params or customized params
def merge_dict(default: dict, overwrite: dict):
    config = {}
    update_config(config, default)
    update_config(config, overwrite)
    return config

# creation of rule
def run_example(input, output, params, **kwargs):
    """
        Hello World, this is a docstring
    """
    params = merge_dict(DEFAULT_PARAMS, params)

    shell(f"""
    echo \"input: {input}
    input.one: {input.one}
    input.two: {input.two}
    outputs: {output}
    output: {output.one}
    output: {output.two}
    params one: {params['one']}
    params two: {params['two']}
    \"
    touch {output.done}
    touch {output}
    touch {output.one}
    touch {output.two}""")
    
####
# END 

