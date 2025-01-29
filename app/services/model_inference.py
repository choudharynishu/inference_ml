import pickle as pk
from pathlib import Path

from config.config import settings
from loguru import logger


class ModelInferenceService:
    """
    A service class for making predictions.

    This class provides functionalities to load the ML model from
    a specified path, and make predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.
        model_path: Directory to extract the model from.
        model_name: Name of the saved model to use.

    Methods:
        __init__: Constructor that initializes the ModelService.
        load_model: Loads the model from file.
        predict: Makes a prediction using the loaded model.
    """

    def __init__(self) -> None:
        """Initialize the ModelInferenceService."""
        self.model = None
        self.model_name = settings.model_name
        self.model_path = settings.model_path

    def load_model(self) -> None:
        """
        Load the model from a specified path.

        Raises:
            FileNotFoundError: If the model file not exist at specified dir.
        """
        logger.info(f"Checking model config file at "
                    f"{self.model_path}/{self.model_name}")
        model_path = Path(f'{self.model_path}/{self.model_name}',
                          )

        if not model_path.exists():
            logger.warning(f"Model at {self.model_path} not found -> "
                           f"building {self.model_name}")
            raise FileNotFoundError(f'Model file at specified '
                                    f'{self.model_path}/{self.model_name} '
                                    f'does not exist')

        logger.info(f"Model {model_path} exists! -> "
                    f"loading model configuration file!")

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

    def predict(self, input_parameters: list) -> list:
        """
        Make a prediction using the loaded model.

        Takes input parameters and passes it to the model, which
        was loaded using a pickle file.

        Args:
            input_parameters (list): The input data for making a prediction.

        Returns:
            list: The prediction result from the model.
        """

        logger.info(f"{"Making predictions"}")
        print(self.model.n_features_in_)
        return self.model.predict([input_parameters]).tolist()
