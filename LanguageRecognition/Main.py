import os

import Settings
from Layer import Layer

layer = Layer()

for f in os.listdir(Settings.TEST_DIR):
    if os.path.isfile(Settings.TEST_DIR + f):
        print(f, layer.test_output(Settings.TEST_DIR + f))

