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

# Snakemake rule
rule example_rule:
    message: """---Rule message---"""
    input:
        INPUT+"first_input", INPUT+"second_input",
        one = INPUT+"hello_input",
        two = INPUT+"world_input"
    output:
        OUTPUT+"first_output", OUTPUT+"second_output",
        one = OUTPUT+"hello_output",
        two = OUTPUT+"world_output",
        done = OUTPUT+"done.txt"
    params:
        two = 'three'
    run:
        params = merge_config(DEFAULT_PARAMS, params)
        options = merge_config(DEFAULT_OPTIONS, {"one": "i am option"})

        shell(f"""echo \"options: one={options['one']}, two={options['two']}
input: {input}
input.one: {input.one}
input.two: {input.two}
outputs: {output}
output: {output.one}
output: {output.two}
params one: {params['one']}
params two: {params['two']}
options:
\" 
touch {output.done}
touch {output}
touch {output.one}
touch {output.two}""")

####
# END 

