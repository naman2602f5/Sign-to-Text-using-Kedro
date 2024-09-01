"""
This is a boilerplate pipeline 'model_prediction'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import predict


def create_pipeline():
    return Pipeline(
        [
            node(
                func=predict,
                inputs=["final_model","params:image_path"],
                outputs=None,
                name="predict"
            )
        ]
    )
