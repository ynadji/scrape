from scrape import *
import sys,os

def basic(region, tag, attr, content=None, usealltags=False):
    if usealltags:
        alltags = region.alltags(tag)
    else:
        alltags = region.all(tag, content)
    for r in alltags:
        try:
            print(s.resolve(r.__getitem__(attr)))
        except Exception as e:
            sys.stderr.write(str(e) + '\n')
