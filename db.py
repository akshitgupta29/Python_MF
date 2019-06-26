"""
To try the DB connectivity for Oracle from Python
"""

import cx_Oracle as db

con = db.connect ('akshit/akshit@localhost/XE')

version = con.version

print(version)

con.close()