import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

def evaluate_model(model, X_test, y_test):
    """
    Model performansını değerlendirir.
    """
    print("Model değerlendirmesi başlıyor...")
    
    # Test verisi üzerinde tahmin yapma
    y_pred = model.predict(X_test)
    y_pred_binary = (y_pred > 0.5).astype(int)
    
    # Sınıflandırma raporu
    print("\n" + "="*50)
    print("SINIFLANDIRMA RAPORU")
    print("="*50)
    report = classification_report(y_test, y_pred_binary, 
                                  target_names=['Good', 'Defective'])
    print(report)
    
    # Karmaşıklık matrisi
    cm = confusion_matrix(y_test, y_pred_binary)
    print("\nKarmaşıklık Matrisi:")
    print(cm)
    
    # Doğruluk hesaplama
    test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
    print(f"\nTest Doğruluğu: {test_accuracy:.4f}")
    print(f"Test Kaybı: {test_loss:.4f}")
    
    return test_accuracy, test_loss, y_pred_binary

def evaluation_pipeline(model, X_test, y_test):
    """
    Ana değerlendirme pipeline'ı - main.py tarafından çağrılacak
    """
    return evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    # Test için
    from data_preprocessing import prepare_data
    from model import create_model
    
    X_train, X_test, y_train, y_test = prepare_data("../data")
    model = create_model()
    evaluation_pipeline(model, X_test, y_test)