import mapbox_vector_tile

import tilereduce


class TRBuildingCount(tilereduce.TR):
    def mapper(self, x, y, zoom, data):
        if data is None:
            return 0

        tile = mapbox_vector_tile.decode(data)

        count = 0
        if tile.get('buildings'):
            count += len(tile['buildings'])
        if tile.get('roads'):
            count += len(tile['roads'])

        return count


if __name__ == '__main__':
    TRBuildingCount.main()
