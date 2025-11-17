# #!/usr/bin/env python3
# """
# Prediction script for Iris classifier
# """

# import sys
# import os
# import numpy as np

# from model import IrisClassifier
# from data_loader import get_target_names

# def main():
#     print("Iris Classifier Prediction")

#     # Load model
#     try:
#         classifier = IrisClassifier()
#         classifier.load_model('models/iris_classifier.pkl')
#         print("Model loaded successfully!")
#     except FileNotFoundError:
#         print("Model not found. Please run train.py first.")
#         return

#     # Get target names
#     target_names = get_target_names()

#     # Example predictions
#     print("\n Example Predictions:")
#     print("Features: [sepal length, sepal width, petal length, petal width]")

#     # Example data for prediction
#     examples = [
#         [5.1, 3.5, 1.4, 0.2],  # Setosa
#         [6.7, 3.0, 5.2, 2.3],  # Virginica
#         [5.9, 3.0, 4.2, 1.5],  # Versicolor
#     ]

#     for i, features in enumerate(examples, 1):
#         prediction = classifier.predict([features])[0]
#         probability = classifier.model.predict_proba([features])[0]

#         print(f"\nExample {i}: {features}")
#         print(f"Prediction: {target_names[prediction]}")
#         print("Probabilities:")
#         for j, prob in enumerate(probability):
#             print(f"  {target_names[j]}: {prob:.4f}")

# if __name__ == "__main__":
#     main()
import sys
import os
import numpy as np

# Add parent directory to path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from data_loader import load_iris_data  # noqa: E402
from model import IrisClassifier  # noqa: E402


class TestIrisClassifier:
    def setup_method(self):
        """Setup method that runs before each test"""
        self.X_train, self.X_test, self.y_train, self.y_test = (
            load_iris_data(test_size=0.3, random_state=42)
        )
        self.classifier = IrisClassifier()

    def test_model_initialization(self):
        """Test that model initializes correctly"""
        assert not self.classifier.is_trained
        assert self.classifier.model is not None

    def test_model_training(self):
        """Test model training functionality"""
        self.classifier.train(self.X_train, self.y_train)
        assert self.classifier.is_trained

    def test_model_prediction(self):
        """Test model prediction functionality"""
        self.classifier.train(self.X_train, self.y_train)
        predictions = self.classifier.predict(self.X_test[:5])
        assert len(predictions) == 5
        assert all(
            isinstance(pred, (np.int32, np.int64, int))
            for pred in predictions
        )

    def test_model_evaluation(self):
        """Test model evaluation functionality"""
        self.classifier.train(self.X_train, self.y_train)
        accuracy, report = self.classifier.evaluate(self.X_test, self.y_test)

        assert 0 <= accuracy <= 1
        assert isinstance(report, str)
        assert "precision" in report.lower()

    def test_model_save_load(self, tmp_path):
        """Test model saving and loading"""
        self.classifier.train(self.X_train, self.y_train)

        # Save model
        save_path = tmp_path / "test_model.pkl"
        self.classifier.save_model(str(save_path))
        assert save_path.exists()

        # Load model
        new_classifier = IrisClassifier()
        new_classifier.load_model(str(save_path))
        assert new_classifier.is_trained

        # Verify predictions match
        original_pred = self.classifier.predict(self.X_test[:5])
        loaded_pred = new_classifier.predict(self.X_test[:5])
        assert np.array_equal(original_pred, loaded_pred)


def test_data_loading():
    """Test data loading functionality"""
    X_train, X_test, y_train, y_test = load_iris_data()

    assert X_train.shape[1] == 4  # 4 features
    assert len(np.unique(y_train)) == 3  # 3 classes
    assert len(X_train) + len(X_test) == 150  # Total samples
