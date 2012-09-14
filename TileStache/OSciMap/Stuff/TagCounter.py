'''
Created on Aug 13, 2012

@author: jeff
'''

import sqlite3 as lite
import sys


try:
    con = lite.connect('/home/jeff/taginfo-db.db')

    cur = con.cursor()  

    #cur.execute('''SELECT key, value, count_all  FROM tags WHERE count_all > 5000 and key not like 'tiger%' and not key like 'addr%' and not key like '3dshapes%'  and not key like 'kms%' and key not in ('note', 'source', 'comment') and not key like 'osak%' order by key, count_all ''')
    
    cur.execute('''SELECT key, value, count_all  FROM tags WHERE count_all > 1000 and key in ('natural', 'waterway', 'surface', 'oneway', 
                    'tunnel', 'service', 'railway', 'shop', 'place', 'boundary', 'admin_level', 'aeroway', 'amenity', 'access', 'abutters', 
                    'barrier', 'bench', 'bicycle', 'bridge', 'building', 'entrance', 'highway', 'landuse', 'leisure', 'man_made', 'route', 'tourism', 
                    'tracktype', 'wetland', 'wood', 'wheelchair') order by count_all desc''')
    
    rows = cur.fetchall()
    
    strings = {}
    tags = ","
    taglist = []
    for row in rows:
        key = row[0].encode('utf-8')
        val = row[1].encode('utf-8')
 
        if not strings.has_key(key):
            strings[key] = key.replace(';','_').replace('/','_').replace('-','_').replace('/','_').replace('?','what').replace(':','_').replace('*','any')
       
        if not strings.has_key(val):
            strings[val] =  val.replace(';','_').replace('/','_').replace('-','_').replace('/','_').replace('?','what').replace(':','_').replace('*','any')
            
        taglist.append('new Tag(s_%s,s_%s,true)' %(strings[key],strings[val]))
        
    print tags.join(taglist) 
        
    print '----------------------'
    for str in strings.iteritems():
        print 'private static final String s_%s = "%s".intern();' %(str[1],str[0])   
    print '----------------------'
    cnt = 0    
    for row in rows:
        print '("%s", "%s"): %d,' %(row[0].encode('utf-8'), row[1].encode('utf-8'), cnt)
        cnt += 1
        
    print len(rows)
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close() 
        
        
