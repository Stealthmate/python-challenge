# http://www.pythonchallenge.com/pc/def/peak.html
import builtins
import io
import pickle  # noqa

import requests

URL = "http://www.pythonchallenge.com/pc/def/banner.p"
data = requests.get(URL, timeout=1000).content

safe_builtins = {
    "range",
    "complex",
    "set",
    "frozenset",
    "slice",
}


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        # Forbid everything else.
        raise pickle.UnpicklingError(f"global '{module}.{name}' is forbidden")


unpickled = RestrictedUnpickler(io.BytesIO(data)).load()
for entry in unpickled:
    for char, count in entry:
        print(char * count, end="")
    print()

target = "channel"
print(f"http://www.pythonchallenge.com/pc/def/{target}.html")
