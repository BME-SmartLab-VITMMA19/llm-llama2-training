# 2nd task evaluation
import os
import sys
import traceback

filename = "llm_task_02.txt"
assert os.path.isfile(filename), "File %s not found!" % filename
with open(filename, "r") as file:
  model = file.read()
  try:
    assert 'Linear(in_features=4096, out_features=8, bias=False)' in model, "Lora rank is not 8 in your model."
    print('Task 2 was successful!')
  except AssertionError:
    _, _, tb = sys.exc_info()
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    print(text)