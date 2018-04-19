import os
import arrow

filesPath = '.'
criticalTime = arrow.now().shift(days=-4)

with os.scandir(filesPath) as rit:
    for entry in rit:
        if not entry.name.startswith('.') and entry.is_dir():
            itemTime = arrow.get(entry.stat().st_mtime)
            print('%s - %s' % (entry.path, itemTime))