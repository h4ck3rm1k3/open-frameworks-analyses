import sys
import csv
import pprint
import json
import codecs
import time
import os
import argparse

seen = {}
for x in ['results.csv.bck','results_framework.csv','results_game.csv','results_games.csv','results_web.csv']:
    print x
    f = open( x)
    d = csv.DictReader(f, dialect=csv.excel, delimiter=";")
    for y in d:
        if y['ordinal_id'] not in seen :
            seen[y['ordinal_id']]=1
            print y['project_name'],y['ordinal_id']
