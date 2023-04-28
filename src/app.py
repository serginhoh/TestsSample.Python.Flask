from flask import Flask

app = Flask(__name__)

app.config.update(
    FLASK_PYDANTIC_API_RENDER_ERRORS = True,
    FLASK_PYDANTIC_API_ERROR_STATUS_CODE  = 422
)

import src.routes.v1.pessoas
