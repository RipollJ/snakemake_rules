# Author: JR & FC
# Created: 2020-05-12
# License: MIT


# Import for snakemake
from lib.utils import snakemake_vars, merge_dict, merge_strings
from snakemake.shell import shell


# define default params
DEFAULT_PARAMS = {"one": "one", "two": "two"}

snakemake_vars(globals(), snakemake)

params = merge_dict(DEFAULT_PARAMS, params)


# creation of rule
echo_message = merge_strings(f"input: {input}",
                             f"input.one: {input.one}",
                             f"input.two: {input.two}",
                             f"outputs: {output}",
                             f"output: {output.one}",
                             f"output: {output.two}",
                             f"params one: {params['one']}",
                             f"params two: {params['two']}", join_string="\n")
# echo_message :
# input: inputs/first_input inputs/second_input inputs/hello_input inputs/world_input
# input.one: inputs/hello_input
# input.two: inputs/world_input
# outputs: outputs/first_output outputs/second_output outputs/hello_output outputs/world_output outputs/done.txt
# output: outputs/hello_output
# output: outputs/world_output
# params one: one
# params two: qsdmflkjqsdml

shell(f"""
echo "{echo_message}"
touch {output.done}
touch {output}
touch {output.one}
touch {output.two}
""")

####
# END
