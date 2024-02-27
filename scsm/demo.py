from SCSM.logger import logging
from SCSM.exception import SCSMException
import sys

try:
    print('Changes done!')
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise SCSMException(e, sys) from e