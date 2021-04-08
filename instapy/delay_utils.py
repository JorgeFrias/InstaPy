import random
from .time_util import sleep

class Delayer:

    @staticmethod
    def random_delay(delayRange: (int, int), logger = None):
        # Sleep a random time based on the range provided after a follow
        delay = random.randint(delayRange[0], delayRange[1])
        if (logger is not None):
            logger.info("Sleeping: {}\n".format(delay))
        sleep(delay)