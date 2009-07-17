#!/usr/bin/env python

# Classic Decorate-Sort-Undecorate
# From an answer I posted to StackOverflow:
#   http://stackoverflow.com/questions/1143671/python-sorting-list-of-dictionaries-by-multiple-keys/1144405

def multikeysort(items, columns):
    from operator import itemgetter
    comparers = [ ((itemgetter(col[1:].strip()), -1) if col.startswith('-') else (itemgetter(col.strip()), 1)) for col in columns]
    def sign(a, b):
        if   a < b:  return -1
        elif a > b:  return 1
        else:        return 0    
    def comparer(left, right):
        for fn, mult in comparers:
            result = sign(fn(left), fn(right))
            if result:
                return mult * result
        else:
            return 0
    return sorted(items, cmp=comparer)

if __name__ == '__main__':    
    b = [{u'TOT_PTS_Misc': u'Utley, Alex', u'Total_Points': 96.0},
     {u'TOT_PTS_Misc': u'Russo, Brandon', u'Total_Points': 96.0},
     {u'TOT_PTS_Misc': u'Chappell, Justin', u'Total_Points': 96.0},
     {u'TOT_PTS_Misc': u'Foster, Toney', u'Total_Points': 80.0},
     {u'TOT_PTS_Misc': u'Lawson, Roman', u'Total_Points': 80.0},
     {u'TOT_PTS_Misc': u'Lempke, Sam', u'Total_Points': 80.0},
     {u'TOT_PTS_Misc': u'Gnezda, Alex', u'Total_Points': 78.0},
     {u'TOT_PTS_Misc': u'Kirks, Damien', u'Total_Points': 78.0},
     {u'TOT_PTS_Misc': u'Worden, Tom', u'Total_Points': 78.0},
     {u'TOT_PTS_Misc': u'Korecz, Mike', u'Total_Points': 78.0},
     {u'TOT_PTS_Misc': u'Swartz, Brian', u'Total_Points': 66.0},
     {u'TOT_PTS_Misc': u'Burgess, Randy', u'Total_Points': 66.0},
     {u'TOT_PTS_Misc': u'Smugala, Ryan', u'Total_Points': 66.0},
     {u'TOT_PTS_Misc': u'Harmon, Gary', u'Total_Points': 66.0},
     {u'TOT_PTS_Misc': u'Blasinsky, Scott', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Carter III, Laymon', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Coleman, Johnathan', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Venditti, Nick', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Blackwell, Devon', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Kovach, Alex', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Bolden, Antonio', u'Total_Points': 60.0},
     {u'TOT_PTS_Misc': u'Smith, Ryan', u'Total_Points': 60.0}]
    
    print "Descending points, ascending name"
    for item in multikeysort(b, ['-Total_Points', 'TOT_PTS_Misc']):
        print item
    
    print
    print "Ascending points, descending name"
    for item in multikeysort(b, ['Total_Points', '-TOT_PTS_Misc']):
        print item

    print
    print "Descending name, ascending points"
    for item in multikeysort(b, ['-TOT_PTS_Misc', 'Total_Points' ]):
        print item
