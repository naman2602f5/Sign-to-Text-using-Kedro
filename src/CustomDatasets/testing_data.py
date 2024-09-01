from tensorflow.keras.preprocessing.image import ImageDataGenerator
from kedro.io import AbstractDataset


class ImageDataGeneratorDataset(AbstractDataset):
    def __init__(self, filepath: str, **kwargs):
        self.filepath = filepath
        self.kwargs = kwargs
        self.datagen = ImageDataGenerator(rescale=1./255)

    def _load(self):
        return self.datagen.flow_from_directory(self.filepath, target_size=[128,128], batch_size=10,
                                                     color_mode='grayscale', class_mode='categorical')

    def _save(self, data):
        raise NotImplementedError("Saving is not supported for ImageDataGeneratorDataset")

    def _describe(self):
        return dict(filepath=self.filepath, **self.kwargs)
