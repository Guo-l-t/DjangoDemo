from polls.models import *

try:
    Question.create_table()
    Choice.create_table()
except:
    pass