import logging
import os

# logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)
log = logging.getLogger(__name__)


def handler(event, context):
    log.debug("Received event {}".format(event))
    log.debug("Testing new version {}".format(context.function_version))
    log.info("Lambda executed")
    return {"Response":f"Sucessfully executed Lambda-1!"}