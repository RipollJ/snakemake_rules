from lib.example_run_fn import run_example
from lib.utils import inject
# ln -s -r lib/ workflow/

INPUT = "inputs/"
OUTPUT = "outputs/"

# rule run_fn
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
        two = 'qsdmflkjqsdml'
    shell:
        inject(run_example,  locals())

rule all:
    # Aim: The last output file of pipeline
    input:
        rules.example_rule.output
