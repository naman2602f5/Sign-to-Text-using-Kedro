"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines import build_model, train_model, model_prediction

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    build_model_pipeline = build_model.create_pipeline()
    train_model_pipeline = train_model.create_pipeline()
    model_prediction_pipeline = model_prediction.create_pipeline()

    return {
        "build_model": build_model_pipeline,
        "train_model": train_model_pipeline,
        "model_prediction": model_prediction_pipeline,
        "__default__": build_model_pipeline + train_model_pipeline + model_prediction_pipeline
    }
