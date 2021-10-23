# rotating file handler to keep log file small with most recent logs

# import logging
# from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# # roll over after 2kb and keep backup logs
# handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=6)
# logger.addHandler(handler)

# for i in range(100000):
#     logger.info("This is the log message")


# timeRotating logger if logger will last for very long time
import time
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler(
    "timed_test.log", when="s", interval=5, backupCount=3)
logger.addHandler(handler)


for i in range(6):
    logger.info("This is the timed logge message")
    time.sleep(5)
