import logging, sys

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

for x in range(0,51,10):
    print("Level-Value:",f"{x:2}", "", logging.getLevelName(x))