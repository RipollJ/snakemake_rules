# For test
# Comment rules that do not use


from lib.example_run_fn import run_example
from pprint import pprint

INPUT = "inputs/"
OUTPUT = "outputs/"

# Custom lib to import


#######################################################################
# rule create

rule first:
    output:
        touch(OUTPUT+"first.done")
    shell:
        'snakemake -p -j 1 -s workflow/first.py -n'


#######################################################################
rule all:
    input:
        rules.first.output

#######################################################################
# END
