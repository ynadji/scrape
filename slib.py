from scrape import *
import sys,os

def basic(region, tag, attr, content=None, usealltags=False, parsethumb=False):
    if usealltags:
        alltags = region.alltags(tag)
        # If we are parsing img with usealltags, we may want to grab the linked
        # image if its a thumbnail.
        if parsethumb:
            fullsize = []
            for t in alltags:
                try:
                    fullsize.append(t.enclosing('a'))
                except ScrapeError:
                    pass
            alltags = fullsize
            # Now we want the enclosing anchor tag's href (link to fullsize).
            attr = 'href'
    else:
        alltags = region.all(tag, content)
    for r in alltags:
        try:
            print(s.resolve(r.__getitem__(attr)))
        except Exception as e:
            sys.stderr.write(str(e) + '\n')
