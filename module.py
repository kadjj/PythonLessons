"""
A module can be deduced as a library
Each file .py is treated as a module

import <<filename>> # imports everything from a file
    import os
    import math
import <<filename>> as <<alias>> #renaming a module
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

from <<filename>> import <<Class, function>> #import specific items
    from collections import Counter

"""

from functions import my_name
my_name("Kadipadi", 200)
