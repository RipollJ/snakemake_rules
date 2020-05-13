# Author: JR & FC
# Created: 2020-05-12
# License: MIT

# Import for snakemake
from snakemake.utils import update_config

# define default params
DEFAULT_PARAMS = {"one": "one", "two": "two"}
DEFAULT_OPTIONS = {'one': "one", "two": "two"}

# merge configuration to choose default params or customized params
def merge_config(default: dict, overwrite: dict):
    config = {}
    update_config(config, default)
    update_config(config, overwrite)
    return config

# creation of rule
def create_example(input, output, params=DEFAULT_PARAMS, options=DEFAULT_OPTIONS):
    """ 
    Description of create_example
    input = input files
    output = output path for output files
    params
    options
    """

    # Snakemake rule
    params = merge_config(DEFAULT_PARAMS, params)
    options = merge_config(DEFAULT_OPTIONS, options)

    rule example_rule:
        message: """---Rule message---"""
        input: **input  # unpacks a dictionary into keyword arguments
        output: **output  
        params: **params  
        shell:
            f"""echo \"options: one={options['one']}, two={options['two']}
input: {{input}}
input.one: {{input.one}}
input.two: {{input.two}}
outputs: {{output}}
output: {{output.one}}
output: {{output.two}}
params one: {{params.one}}
params two: {{params.two}}
\" 
touch {{output.done}}
touch {{output}}
touch {{output.one}}
touch {{output.two}}"""

####
# END 

