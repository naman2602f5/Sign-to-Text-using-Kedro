"""
This is a boilerplate pipeline 'train_model'
generated using Kedro 0.19.8
"""
import pickle
import mlflow

def train_model(model, epochs, training_data, testing_data):
    model.fit(training_data, epochs=epochs, validation_data=testing_data)
    return model


def save_model(model):
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="model_new",
    )
    return model