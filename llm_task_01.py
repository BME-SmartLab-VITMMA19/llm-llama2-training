# 1st task evaluation
import os
import sys
import traceback

filename = "llm_task_01.txt"
assert os.path.isfile(filename), "File %s not found!" % filename
with open(filename, "r") as file:
  content = file.read()
  parsed = content.split('\n')
  try:
    assert int(parsed[0])>10, "Length of training dataset is less than the required."
    print('Task 1 was successful!')
  except AssertionError:
    _, _, tb = sys.exc_info()
    tb_info = traceback.extract_tb(tb)
    filename, line, func, text = tb_info[-1]
    print(text)