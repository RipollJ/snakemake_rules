from snakemake.utils import update_config
from snakemake.io import Params


class Param(str):
    """ Represents a ghost parameter, will return False and is equal to None is represented as a snakemake object eg: {params.example}
    """

    def __eq__(self, other):
        return None == other

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False


class StubParams(Params):
    """ Represents an empty Params object, will return False or will delegate resolution to snakemake
    """

    def __init__(self, prefix):
        self.__prefix = prefix

    def __stub_param(self, key):
        return Param("{"+self.__prefix+"."+key+"}")

    def __getitem__(self, key):
        return self.__stub_param(key)

    def __getattr__(self, key):
        return self.__stub_param(key)

    def __str__(self):
        return "{"+self.__prefix+"}"
    
    def get(self, key, default=""):
        return default;


STUB_SNAKEMAKE_VARS = {
    "input": StubParams("input"),
    "log": StubParams("log"),
    "output": StubParams("output"),
    "params": StubParams("params"),
    "resources": StubParams("resources"),
    "rule": StubParams("rule"),
    "threads": StubParams("threads"),
    "wildcards": StubParams("wildcards")
}


def inject(fn, snakemake_vars):
    """ Injects snakemake variables into the function. If snakemake vars cannot be resolved, injects a ghost object which impersonate snakemake variables, always returning false
    """
    if 'rule' in snakemake_vars:
        shell_command = fn(**snakemake_vars)
        print(shell_command)
        return shell_command
    else:
        return "WARNING : snakemake values are not currently available, can result in inconsistencies in the displayed shell command.\n"+fn(**STUB_SNAKEMAKE_VARS)


def merge_dict(default, overwrite):
    """Merges default and overwrite into an new object.
    """
    print('Deprecation: merge_dict is now deprecated')
    if isinstance(overwrite, StubParams):
        return Params(fromdict=default)

    config = {}
    update_config(config, default)
    update_config(config, overwrite)
    return Params(fromdict=config)


def join_str(*args, joiner=" \\\n"):
    """ Joins argument strings using joiner attribute.

    Will ignore Falsy strings

    *args:
        strings to join together

    returns:
        the joined string
    """
    return joiner.join(filter(None, args))


def merge_strings(*args, join_string=" \\\n"):
    print('Deprecation: merge_strings is now deprecated, use join_str(*args, joiner=" ") instead: join_str("a", "b", "c", joiner=",")')
    return join_str(*args, joiner=join_string)


def optional(holder, string, variable, default_value=False):
    value = holder.get(variable, default_value)
    return string.format(value) if value else ""


def is_fasta(input_fasta):
    for suffix in ['.fa', '.fna', '.fas', '.fasta', '.fa.gz', '.fna.gz', '.fas.gz', '.fasta.gz']:
        if input_fasta.endswith(suffix):
            #self.importFasta(input_fasta)
            return True
        else: 
            return (self, "Input file format not right", warn_msg)
    warn_msg = (
                "Please, drag a fasta formatted sequence file with .fa, .fna, .fas, .fasta, "
                ".fa.gz, .fna.gz, .fas.gz, .fasta.gz suffix"
            )


def is_gff3(annotation_path):
    for gsuffix in ['.gff', '.gff3.gz', '.gff3']:
        #extension = os.path.splitext(annotation_path)[1]
        if annotation_path.endswith(tuple(gsuffix)):
            return True
    else:
        return False
