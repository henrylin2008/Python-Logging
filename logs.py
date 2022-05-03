import logging

logging.basicConfig(level=logging.INFO, filename='log.log', filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
# level: log level, current level and above are included in the log
# filename: file to track the logs; could use time as a part of the file name
# filemode: w: create a new file or overwrite the file if exist
# format: format for the logs: time, level, message; https://docs.python.org/3/library/logging.html#logrecord-attributes

# logging.debug("debug")          # less important
# logging.info("info")
# logging.warning('warning')      # default: warning and above (error, critical)
# logging.error('error')
# logging.critical('critical')    # most important

# exception log
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     logging.exception("ZeroDivisionError")  # logs the exception
#     # logging.error("ZeroDivisionError", exc_info=True)


# Custom Logs
logger = logging.getLogger(__name__)      # retrieve logger with the name or create it for you
# Handles and formatters
handler = logging.FileHandler('test.log')   # FileHandler: name of the file
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")   # custom format of the logs
handler.setFormatter(formatter)         # set the formatter of the handler

logger.addHandler(handler)

logger.info("test the custom logger")
