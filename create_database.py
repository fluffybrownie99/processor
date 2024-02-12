import sqlite3

conn = sqlite3.connect('stats.sqlite')

c = conn.cursor()
c.execute(
    '''
    CREATE TABLE ServerStats (
    id INTEGER PRIMARY KEY,
    total_uploads INTEGER,
    total_playbacks INTEGER,
    most_accessed_file_id INTEGER,
    largest_file_id INTEGER,
    last_updated DATETIME);
    '''
)