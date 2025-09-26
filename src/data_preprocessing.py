import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split

def prepare_data(data_dir, img_size=(224, 224), test_size=0.2, random_state=42):
    """
    Veri setini yükler, ön işler ve eğitim/test setlerine ayırır.
    """
    images = []
    labels = []
    
    categories = ['good', 'defective']
    for category in categories:
        path = os.path.join(data_dir, category)
        label = categories.index(category)
        print(f'{category} klasöründeki görüntüler işleniyor...')
        
        for img_name in os.listdir(path):
            try:
                img_path = os.path.join(path, img_name)
                img = cv2.imread(img_path)
                img = cv2.resize(img, img_size)
                images.append(img)
                labels.append(label)
            except Exception as e:
                print(f'{img_name} dosyası işlenirken hata: {e}')
    
    images = np.array(images)
    labels = np.array(labels)
    images = images / 255.0
    
    X_train, X_test, y_train, y_test = train_test_split(
        images, labels, test_size=test_size, random_state=random_state, stratify=labels
    )
    
    print('Veri hazırlığı tamamlandı.')
    return X_train, X_test, y_train, y_test

def data_preparation_pipeline():
    """
    Ana veri hazırlama pipeline'ı - main.py tarafından çağrılacak
    """
    data_path = "data"
    return prepare_data(data_path)

if __name__ == "__main__":
    # Test için
    X_train, X_test, y_train, y_test = data_preparation_pipeline()
    print(f"Eğitim seti: {X_train.shape}")
    print(f"Test seti: {X_test.shape}")