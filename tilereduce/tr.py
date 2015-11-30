import io
import json
import os
import sys

from . import sources


class TR(object):
    def __init__(self, source):
        self.source = source

    @classmethod
    def main(cls, argv=None):
        if argv is None:
            argv = sys.argv[1:]
        source = get_source(argv[0])

        tr = cls(source)
        tr.send({'ready': True})
        tr.run()

    def send(self, data):
        # file descriptor 3 is used for IPC.
        os.write(3, json.dumps(data) + '\n')

    def run(self):
        # file descriptor 3 is used for IPC.
        # messages are split by newlines
        with io.open(3, newline='\n') as f:
            for line in f:
                tile = map(int, json.loads(line))
                self.run_tile(tile)

    def run_tile(self, tile):
        x, y, zoom = tile
        data = self.source.fetch_tile(x, y, zoom)
        value = self.mapper(x, y, zoom, data)
        self.send({'reduce': True, 'value': value, 'tile': tile});

    def mapper(self, x, y, zoom, data):
        raise NotImplementedError()


def get_source(arg):
    specs = json.loads(arg)
    for spec in specs:
        db = spec.get('mbtiles')
        if db:
            source = sources.MBTiles(db)
            return source
    raise ValueError('Could not create tile source from argument "%s"' % arg)
