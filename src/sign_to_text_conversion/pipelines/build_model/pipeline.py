"""
This is a boilerplate pipeline 'build_model'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import build_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=build_model,
                inputs=["params:input_shape"],
                outputs="model",
                name="build_model"
            ),
        ]
    )