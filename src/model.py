import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def create_model():
    """
    CNN model mimarisini oluşturur.
    """
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, X_train, y_train, X_test, y_test, epochs=15, batch_size=32):
    """
    Modeli eğitir ve geçmişi döndürür.
    """
    model.summary()
    print("Model eğitimi başlıyor...")
    
    history = model.fit(X_train, y_train, 
                       epochs=epochs, 
                       batch_size=batch_size, 
                       validation_data=(X_test, y_test))
    
    print("Model eğitimi tamamlandı.")
    return history

def model_training_pipeline(X_train, y_train, X_test, y_test):
    """
    Ana model eğitim pipeline'ı - main.py tarafından çağrılacak
    """
    model = create_model()
    history = train_model(model, X_train, y_train, X_test, y_test)
    return model, history

if __name__ == "__main__":
    # Test için
    from data_preprocessing import prepare_data
    X_train, X_test, y_train, y_test = prepare_data("../data")
    model, history = model_training_pipeline(X_train, y_train, X_test, y_test)