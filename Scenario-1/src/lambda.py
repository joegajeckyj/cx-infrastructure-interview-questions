import logging
import os

# logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)
log = logging.getLogger(__name__)


def handler(event, context):
    log.debug("Received event {}".format(event))
    log.debug("Testing Release 1")
    log.info("Lambda executed")
    return {f"Sucessfully executed Scenario 1 Lambda!"}