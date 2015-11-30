tilereduce
==========

A framework for writing [tile-reduce](https://github.com/mapbox/tile-reduce)
map scripts in Python.

NOTE: This library is experimental and under active development. No official
release has been created.


Usage
-----
First read the documentation at [tile-reduce](https://github.com/mapbox/tile-reduce).

`tile-reduce-py` allows you to write the map script in Python. The reducer is
still Javascript. These examples require a modification to tile-reduce (see: https://github.com/mapbox/tile-reduce/pull/68)

```
import mapbox_vector_tile

import tilereduce


class BuildingRoadCount(tilereduce.TR):
    def mapper(self, x, y, zoom, data):
        if data is None:
            return 0

        # Decode the raw binary protocol buffer data
        td = mapbox_vector_tile.decoder.TileData(2048)
        tile = td.getMessage(data)

        count = 0
        if tile.get('buildings'):
            count += len(tile['buildings'])
        if tile.get('roads'):
            count += len(tile['roads'])

        return count


if __name__ == '__main__':
    BuildingRoadCount.main()
```

The reduce script is identical as the original Node example except:
* An additional argument `workerCommand` is set to 'python'
* The `map` argument is now the path to the Python map script

```
'use strict';

var tileReduce = require('tile-reduce');
var path = require('path');

var numFeatures = 0;

tileReduce({
  bbox: [-122.05862045288086, 36.93768132842635, -121.97296142578124, 37.00378647456494],
  zoom: 15,
  map: path.join(__dirname, '/count.py'),  // Calling python script
  workerCommand: 'python',
  sources: [{name: 'osm', mbtiles: path.join(__dirname, '../../tests/fixtures/osm.mbtiles'), raw: true}]
})
.on('reduce', function(num) {
  numFeatures += num;
})
.on('end', function() {
  console.log('Features total: %d', numFeatures);
});
```
