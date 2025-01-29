from flask import Blueprint, request, abort
from pydantic import ValidationError

from schema.schema import FMCG
from services import model_inference_service


inference = Blueprint('inference', __name__,)

@inference.route("/pred")
def get_prediction() -> dict:
    """
    Return a prediction based on the query parameters.

    Returns:
        dict: A dictionary containing the prediction result.
    """

    try:
        fmcg_data = FMCG(**request.args)
    except ValidationError:
        abort(400, description=f"Bad input parameters, got: {request.args}")

    predictions = model_inference_service.predict(
        list(fmcg_data.model_dump().values()),
    )

    return {'predictions': predictions}