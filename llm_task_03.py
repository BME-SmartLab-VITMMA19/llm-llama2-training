# 3rd task evaluation
import os
import sys
import traceback

filename = "llm_task_03.txt"
assert os.path.isfile(filename), "File %s not found!" % filename
with open(filename, "r") as file:
  content = file.read()
  parsed = content.split('\n')
  try:
    assert float(parsed[1])<=0.75, "Validation is higher than 0.75"
    print('Task 3 was successful!')
  except AssertionError:
    _, _, tb = sys.exc_info()
    #traceback.print_tb(tb)
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    print(text)