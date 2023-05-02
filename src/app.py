from flask import Flask
from flask_pydantic_api import apidocs_views

app = Flask(__name__)

app.config.update(
    FLASK_PYDANTIC_API_RENDER_ERRORS = True,
    FLASK_PYDANTIC_API_ERROR_STATUS_CODE  = 422
)

app.register_blueprint(apidocs_views.blueprint, url_prefix="/apidocs")

import src.routes.v1.pessoas
