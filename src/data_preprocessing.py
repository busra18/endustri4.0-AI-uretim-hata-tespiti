"""
📊 VERİ ÖN İŞLEME MODÜLÜ
Tekstil görüntülerini hazırlar ve temizler
"""

import numpy as np
import cv2
from sklearn.model_selection import train_test_split

def load_data(data_path):
    """H5 dosyasından veriyi yükler"""
    import h5py
    with h5py.File(data_path, 'r') as f:
        images = np.array(f['images'])
        labels = np.array(f['labels'])
    return images, labels

def preprocess_images(images):
    """Görüntüleri normalize eder ve boyutlandırır"""
    # Normalizasyon: 0-255 -> 0-1
    images = images.astype('float32') / 255.0
    
    # Boyut kontrolü
    if len(images.shape) == 3:
        images = np.expand_dims(images, axis=-1)
        
    return images

def split_data(images, labels, test_size=0.2):
    """Veriyi eğitim ve test olarak ayırır"""
    return train_test_split(images, labels, test_size=test_size, random_state=42)

# Test kodu
if __name__ == "__main__":
    print("🔧 Data preprocessing modülü yüklendi")