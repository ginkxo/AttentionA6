from __future__ import unicode_literals, print_function, division
from io import open

import unicodedata
import string
import re
import random

import torch
import torch.nn as nn
from torch import optim 
import torch.nn.functional as F 

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ----

START_TOKEN = 0
END_TOKEN = 1

class Lang:
	def __init__(self, name):
		pass

	def addSentence(self, sent):
		pass

	def addWord(self, word):
		pass

def unicodeToAscii(s):
	pass

def normalizeString(s):
	pass

def readLands(Lang1, Lang2, reverse=False):
	pass

# ----



