
import logging

logging.basicConfig(
    filename='agent.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Agent started successfully")
logging.warning("Received unexpected query format")
logging.error("NLU module failed to parse query")
