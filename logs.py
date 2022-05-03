import logging

logging.basicConfig(level=logging.INFO, filename='log.log', filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")
# filename: file to track the logs; could use time as a part of the file name
# filemode: w: create a new file or overwrite the file if exist
# format: format for the logs: time, level, message; https://docs.python.org/3/library/logging.html#logrecord-attributes

# logging.debug("debug")          # less important
# logging.info("info")
# logging.warning('warning')      # default: warning and above (error, critical)
# logging.error('error')
# logging.critical('critical')    # most important

try:
    1 / 0
except ZeroDivisionError as e:
    logging.exception("ZeroDivisionError")  # logs the exception
    # logging.error("ZeroDivisionError", exc_info=True)
