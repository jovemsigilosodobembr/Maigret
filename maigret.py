#!/usr/bin/env python3
import asyncio
import sys

from maigret.maigret import main


def run():
    try:
        if sys.version_info.minor >= 10:
            asyncio.run(main())
        else:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
    except KeyboardInterrupt:
        print('Maigret é interrompido.')
        sys.exit(1)


if __name__ == "__main__":
    run()
