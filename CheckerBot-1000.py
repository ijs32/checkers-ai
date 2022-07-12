import os
from MySQLConn.mySQLdb import cnx

import tensorflow as tf
from tensorflow import keras

# the plan --
# create an AI trained solely on regular piece moves to pick a move for the piece board
# create a separate AI trained solely on king piece moves to pick a move for the king board
# create a final general AI trained on sets of games to think more about the big picture and choose the best move from the two sub AIs