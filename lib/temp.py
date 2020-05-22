from pprint import pprint
from utils import optional, extensions, _StubParams, mappy, is_fasta
from snakemake.io import Params

stubbed_params = _StubParams("params")
stubbed_option = optional(stubbed_params, "test", "--tests {}")
stubbed_option1 = optional(stubbed_params, "test", "--tests {}", "hello :)")

pprint(stubbed_option)
pprint(stubbed_option1)


params = Params(fromdict={"test": "yes"})
option = optional(params, "test", "--tests {}")
option1 = optional(params, "test1", "--tests {}")
option2 = optional(params, "test2", "--tests2 {}",
                   default_value="test2_default")
pprint(option)
pprint(option1)


mappy(params, "test2", "test parameter")

mappy(params, "test", ("test parameter", "test parameter2"))
mappy(params, "test", ["test parameter", "test parameter2"])

mappy(params, "test", {"index": "--runGenemome", "run": "test failed"})


def example(file_path):
    result = is_fasta(file_path)
    if result:
        return file_path
    return False


pprint(example("test"))
pprint(is_fasta("test"))

mappy(input, "annot", 'yes')
mappy(params, "test", {"yes2": "test success", "no": "test failed"})
try:
    pprint(mappy(params, "test", "test parameter2"))
except ValueError as err:
    pprint(err)
    pass


try:
    pprint(mappy(params, "test", ("yes", "no")))
except ValueError as err:
    pprint(err)
    pass

try:
    pprint(mappy(params, "test", {
           "yes2": "test success", "no": "test failed"}))
except ValueError as err:
    pprint(err)
