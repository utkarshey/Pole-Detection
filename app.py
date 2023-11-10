from poleDetection.logger import logging
from poleDetection.exception import AppException
import sys

# logging.info("My second log!")

try:
    a = 3 / "s"

except Exception as e:
    raise AppException(e, sys)