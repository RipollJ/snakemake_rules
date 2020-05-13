#!/usr/bin/env python3
from snakemake.utils import update_config


def snakemake_vars(glob, snakemake):
    glob['input'] = snakemake.input
    glob['log'] = snakemake.log
    glob['output'] = snakemake.output
    glob['params'] = snakemake.params
    glob['resources'] = snakemake.resources
    glob['rule'] = snakemake.rule
    glob['threads'] = snakemake.threads
    glob['wildcards'] = snakemake.wildcards


def merge_dict(default: dict, overwrite: dict):
    config = {}
    update_config(config, default)
    update_config(config, overwrite)
    return config


def merge_strings(*args, join_string=" "):
    return join_string.join(filter(None, args))
