# Author: JR & FC
# Created: 2020-05-14
# License: MIT


# Import for snakemake
from snakemake.utils import update_config
from lib.utils import merge_dict, merge_strings

# define default params
DEFAULT_PARAMS = {"one": "one", "two": "two"}

# creation of rule


def run_example(input, output, params, **kwargs):
    """
        Hello World, this is a docstring
    """
    params = merge_dict(DEFAULT_PARAMS, params)

    return merge_strings(f"echo \"input: {input}",
                         f"input.one: {input.one}",
                         f"input.two: {input.two}" if input.two != "{input.two}" else "outputs/testing",
                         f"outputs: {output}",
                         f"output: {output.one}",
                         f"output: {output.two}",
                         f"params: {params}",
                         f"params one: {params.one}",
                         f"params two: {params.two}\"",
                         f"touch {output.done}",
                         f"touch {output}",
                         f"touch {output.one}",
                         f"touch {output.two}", join_string="\n")

####
# END
