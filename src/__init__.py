"""
Tekstil Kusur Tespit Sistemi - AI Modülü
"""

from .data_preprocessing import prepare_data, data_preparation_pipeline
from .model import create_model, train_model, model_training_pipeline

__version__ = "1.0.0"
__author__ = "Endüstri 4.0 AI Takımı"

__all__ = [
    'prepare_data',
    'data_preparation_pipeline',
    'create_model', 
    'train_model',
    'model_training_pipeline'
]