
from lib.example_run_fn import run_example

INPUT = "inputs/"
OUTPUT = "outputs/"

# Custom lib to import
include: "lib/example_rule.py"
include: 'lib/example_run.py'
include: 'lib/example_script.py'

#######################################################################
# rule create
 create_example({"0": INPUT+"first_input", "1": INPUT+"second_input", "one": INPUT+"hello_input", "two": INPUT+"world_input"},
                {"0": OUTPUT+"first_output", "1": OUTPUT+"second_output",
                 "one": OUTPUT+"hello_output", "two": OUTPUT+"world_output", "done": OUTPUT+"done.txt"},
                {"two": "three"},
                {"one": "i am option"})

# rule shell
 rule example_rule:
     message: """---Indexing reference genome---"""
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
         shell(run_example2(input, output, params, wildcards, log, threads,
                            resources, config, options={"one": "i am option"}))

# rule run
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
    run:
        run_example(**locals())

# rule script
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
    script:
        run_example(**locals())
        
#######################################################################
rule all:
    # Aim: Detection of differentially expressed isoforms
    input:
        rules.example_rule.output
        
#######################################################################
# END
