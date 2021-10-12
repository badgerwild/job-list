import sqlite3
from DAO import DAO

db = DAO()

con, cur = db.connect()
# TODO implement checks for each table and create table if they do not exist
# cur.execute(
#    '''SELECT count(name) FROM sqlite_master WHERE type= 'table' AND name ='Job' '''
# )

# if cur.fetchone()[0] == 1:
#    print('TABLE EXISTS')

# else:
#    print('NO TABLE')

cur.execute(
    'CREATE TABLE Apply(job_id INTEGER PRIMARY KEY, status TEXT, submit_date TEXT, response_date TEXT, number_of_interviews INTEGER DEFAULT -1, leet_code BOOLEAN DEFAULT 0 CHECK(leet_code IN(0,1)), code_challenge INTEGER DEFAULT 0 CHECK(code_challenge IN(0,1)), cover_letter BOOLEAN CHECK(cover_letter IN(0,1)), platform TEXT)',
    '')
con.commit()
