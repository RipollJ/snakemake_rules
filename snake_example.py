#!/usr/bin/env python3

######################
# Snakefile_draft.py #
######################

# Author: RipollJ
# Created: 2020-05-25
# License: License CC-BY-NC 4.0
# Last update: 2020-05-25

#######################################################################

# Pre-requisite:
# Use: XXX provided in the environment yaml file

#######################################################################

# execution: snakemake -s [name_snakefile]
# --use-conda [use conda env specified in script&config]
# -j [Number of cores]
# -n [Check integrity: dry mode before execution]
# -p [Print rules script]
# -r [Print the reason for each executed rule]
# if run on a cluster, use --cluster-config Cluster.json

#######################################################################

# import dependencies for snakemake
import os
import sys

# Config file
#configfile: "Config.yml"

# Environment 
ENVIRONMENT1 = "../envs/XXX.yml"   # specify path to environments folder
ENVIRONMENT2 = "../envs/YYY.yml"

# Input folders
INPFOL       = config["INPFOL"]      # specify path to input folder
PROJECT      = config["PROJECTNAME"] # choose your specific project name
PATH         = config["relpath"]     # path for output and input data

# Params
PAIRED     = config["paired"]
THREADS    = config["threads"]["medium"]   # low: 4 CPUs, medium: 8, high: 16, ultra: 32

# Wildcards
SAMPLE, = glob_wildcards(PATH+INPFOL+"{sample}"+("_1" if PAIRED == "YES" else "")+".fastq.gz")

#######################################################################

# conditions for paired-end data or not, change according to rules
fareadss = {}

if PAIRED == "YES":
   fareadss = {"fareads1" : PATH+"out/{project}/FOLDER/folder/{sample}_1.fastq.gz", "fareads2" :PATH+"out/{project}/FOLDER/folder/{sample}_2.fastq.gz"}
else:
    fareadss= {"fareads": PATH+"out/{project}/FOLDER/folder/{sample}.fastq.gz"}


outs = {}

if PAIRED == "YES":
   outs = {"out1" : PATH+"out/{project}FOLDER/folderOut/{sample}_1.format", "out2" :PATH+"out/{project}/FOLDER/folderOut/{sample}_2.format"}
else:
    outs = {"out": PATH+"out/{project}/FOLDER/folderOut/{sample}.format"}

#######################################################################

rule XYZ:
    # Aim: ...
    message:
        "--- Try on {wildcards.sample} ---"
    conda:
        ENVIRONMENT1
    log:
        PATH+"out/{project}/FOLDER/folder/{sample}.log"
    input:
        **fareadss
    params:
        threads  = THREADS
    output:
        **outs
    shell:
        "PROGRAM "
        +("in1={input.fareads1} in2={input.fareads2} " if PAIRED == "YES" else "in={input.fareads} ")
        +("out1={output.out1} out2={output.out2} " if PAIRED == "YES" else "out={output.out} ")
        "threads={params.threads} "
        "2>{log}"

#######################################################################

rule all:
    # Aim: ...
    input:
        final = expand(PATH+"out/{project}/FOLDER/folderOut/{sample}"+("_1" if PAIRED == "YES" else "")+".format",
                            project = PROJECT,
                            sample  = SAMPLE)
