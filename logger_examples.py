import traceback
import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger("simpleExample")
logger.debug("this is just a debug message")


# not used since we create a config for logger in a file, logging.conf

# logger = logging.getLogger(__name__)

# # create handler
# stream_h = logging.StreamHandler() # logs to stream
# file_h = logging.FileHandler("file.log")     # logs to file

# # level for logging and format

# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)


# formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning("this is the warning message")
# logger.error("This is an error message")


# capturing stacktrace

print("\n")

import traceback

try:
    a = [1, 2, 3]
    val = a[0]
except:
    logging.error(f"The error is {traceback.format_exc()}")