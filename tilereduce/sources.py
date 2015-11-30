import gzip
import sqlite3
import StringIO


query = """
    SELECT tile_data FROM tiles WHERE
    tile_column=? AND tile_row=? AND zoom_level=?;
"""


class MBTiles(object):
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)

    def fetch_tile(self, x, y, zoom):
        # Flip the row due to MBTiles using TMS row/tile spec
        y = 2**zoom - 1 - y

        cursor = self.conn.cursor()
        cursor.execute(query, (x, y, zoom))
        # There should at most one tile so just use fetchone()
        data = cursor.fetchone()
        if data:
            data = uncompress(data[0])
        return data


def uncompress(compressed):
    fileobj = StringIO.StringIO(compressed)
    gz = gzip.GzipFile(fileobj=fileobj, mode='r')
    uncompressed = gz.read(fileobj)
    gz.close()

    return uncompressed
