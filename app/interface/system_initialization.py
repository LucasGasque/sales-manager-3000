import time
from .text_art_bender import bender


def system_initialization():
    time.sleep(0.5)
    print(60 * "-")

    time.sleep(0.5)
    print(
        """
          Welcome to Sales Manager 3000™.
          """
    )

    time.sleep(0.5)
    print(
        """
          Everyone's favorite sales manager.
          """
    )

    for part in bender:
        time.sleep(0.1)
        print(part)

    time.sleep(1)
    print(
        """
          This program is a simple sales manager prototype.
          """
    )

    time.sleep(1)
    print(
        """
          It is free and realy simple to use!
        """
    )

    time.sleep(1)
    print(
        """
          Just follow the instructions...
        """
    )

    time.sleep(1)
    print(
        """
          It's not that hard...
        """
    )

    time.sleep(0.5)
    print(60 * "-")

    time.sleep(1.5)
