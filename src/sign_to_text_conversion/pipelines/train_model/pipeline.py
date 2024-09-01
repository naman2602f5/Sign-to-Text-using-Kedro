"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.19.8
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import train_model, save_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_model,
                inputs=["model", "params:epochs", "training_data", "testing_data"],
                outputs="trained_model",
                name="train_model"
            ),
            node(
                func=save_model,
                inputs=["trained_model"],
                outputs="final_model",
                name="save_model"
            ),
        ]
    )
