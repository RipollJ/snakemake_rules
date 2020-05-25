## Snakemake rules

- Aim: optimize creation of new pipelines and avoid copy paste
- How: exploiting the potential of python

### Rules builder
- example_rule: use a function to create a rule, problem lack of visibility in the main.py
- example_run: use shell to create rule from the run snakemake command
- example_run_fn: run a function to create the snakemake rule
- example_script: use script to create the rule with snakemake shell import

### how to test
```shell
snakemake \
    -s main.py \ # script to execute, call the others
    -j 1 \ # number of cores
    --force-all \ # force execution 
    -p \ # print script
    --debug \ # to see debug output
    -n # dry_run
```

### Warnings snakemake v5.15
Conda environments are only allowed with shell, script, notebook, or wrapper directives (not with run).
