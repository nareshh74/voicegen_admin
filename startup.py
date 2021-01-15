# 3rd party modules
import uvicorn

# applicaion modules
from src.application import app
from src.config import config


if __name__ == "__main__":
    uvicorn.run(app, host=config.host, port=config.port, debug=True, log_level="trace") 
