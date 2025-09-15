#!/usr/bin/env python3
"""
Kütüphane Kurulum Kontrol Scripti
Bu script, proje için gerekli tüm kütüphanelerin doğru kurulup kurulmadığını kontrol eder.
"""

import importlib
import sys
import subprocess
import platform

def print_header(text):
    """Başlık yazdırma fonksiyonu"""
    print("\n" + "="*60)
    print(f"🔧 {text}")
    print("="*60)

def print_separator():
    """Ayraç yazdırma fonksiyonu"""
    print("-" * 60)

def check_module(module_name, version=None, pip_name=None):
    """
    Bir modülün kurulu olup olmadığını kontrol eder
    
    Args:
        module_name (str): Modül adı
        version (str, optional): Beklenen versiyon
        pip_name (str, optional): Pip'deki farklı adı
    
    Returns:
        tuple: (kurulu_mu, versiyon)
    """
    try:
        module = importlib.import_module(module_name)
        actual_version = getattr(module, '__version__', 'Bilinmiyor')
        
        if version:
            # Sadece ana ve alt versiyon numaralarını karşılaştır
            expected_major_minor = '.'.join(version.split('.')[:2])
            actual_major_minor = '.'.join(str(actual_version).split('.')[:2])
            
            if actual_major_minor == expected_major_minor:
                status = "✅"
            else:
                status = "⚠️ "
                
            print(f"{status} {module_name}: {actual_version} (beklenen: {version})")
            return (True, actual_version)
        else:
            print(f"✅ {module_name}: {actual_version}")
            return (True, actual_version)
            
    except ImportError:
        print(f"❌ {module_name}: Yüklü değil")
        return (False, None)

def get_system_info():
    """Sistem bilgilerini alır"""
    system_info = {
        "İşletim Sistemi": platform.system(),
        "İşletim Sistemi Versiyonu": platform.version(),
        "Python Versiyonu": platform.python_version(),
        "İşlemci": platform.processor(),
    }
    return system_info

def install_missing_modules(missing_modules):
    """Eksik modülleri kurar"""
    if not missing_modules:
        return True
        
    print_header("EKSİK MODÜLLERİ KURMA")
    
    for module, pip_name in missing_modules:
        print(f"📦 {module} kuruluyor...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name or module])
            print(f"✅ {module} başarıyla kuruldu")
        except subprocess.CalledProcessError:
            print(f"❌ {module} kurulumu başarısız")
            return False
            
    return True

def main():
    """Ana fonksiyon"""
    print_header("KAPADOKYA ÜNİVERSİTESİ - YAPAY ZEKÂ PROJESİ")
    print("🔍 Kütüphane kurulum kontrolü başlatılıyor...")
    
    # Sistem bilgilerini göster
    system_info = get_system_info()
    print("\n💻 SİSTEM BİLGİLERİ:")
    for key, value in system_info.items():
        print(f"   {key}: {value}")
    
    print_separator()
    
    # Kontrol edilecek modüller listesi
    # (modül_adı, beklenen_versiyon, pip_adı)
    modules_to_check = [
        ("tensorflow", "2.13.0", None),
        ("keras", "2.13.1", None),
        ("cv2", "4.8.1", "opencv-python"),
        ("PIL", "10.0.1", "Pillow"),
        ("numpy", "1.24.3", None),
        ("pandas", "2.0.3", None),
        ("sklearn", "1.3.0", "scikit-learn"),
        ("matplotlib", "3.7.2", None),
        ("seaborn", "0.12.2", None),
        ("h5py", "3.9.0", None),
        ("tqdm", "4.66.1", None),
        ("gradio", "3.44.4", None),
        ("jupyter", "1.0.0", None),
        ("notebook", "6.5.4", None),
        ("psutil", "5.9.5", None),
    ]
    
    print("📦 MODÜL KONTROLÜ:")
    missing_modules = []
    all_ok = True
    
    for module, version, pip_name in modules_to_check:
        is_installed, actual_version = check_module(module, version, pip_name)
        if not is_installed:
            missing_modules.append((module, pip_name or module))
            all_ok = False
    
    print_separator()
    
    # GPU kontrolü
    try:
        import tensorflow as tf
        gpu_devices = tf.config.list_physical_devices('GPU')
        if gpu_devices:
            print("🎮 GPU DURUMU: ✅ Kullanılabilir")
            for i, device in enumerate(gpu_devices):
                print(f"   GPU {i}: {device}")
        else:
            print("🎮 GPU DURUMU: ⚠️  Kullanılamıyor (CPU modu)")
    except:
        print("🎮 GPU DURUMU: ❌ TensorFlow yüklü olmadığı için kontrol edilemedi")
    
    print_separator()
    
    # Sonuç raporu
    if all_ok:
        print("🎉 TÜM KONTROLLER TAMAMLANDI: ✅ Başarılı!")
        print("   Tüm gerekli kütüphaneler doğru versiyonlarla yüklü.")
    else:
        print("⚠️  KONTROLLER TAMAMLANDI: ❌ Eksik kütüphaneler bulundu")
        print(f"   Eksik kütüphane sayısı: {len(missing_modules)}")
        
        # Eksik modülleri kurma seçeneği
        response = input("\n❓ Eksik kütüphaneleri şimdi kurmak ister misiniz? (e/h): ")
        if response.lower() in ['e', 'evet', 'y', 'yes']:
            success = install_missing_modules(missing_modules)
            if success:
                print("\n🎉 Tüm eksik kütüphaneler başarıyla kuruldu!")
                print("   Lütfen scripti yeniden çalıştırarak kontrol edin.")
            else:
                print("\n❌ Kurulum sırasında hata oluştu!")
                print("   Lütfen manuel olarak kurmayı deneyin.")
        else:
            print("\nℹ️  Eksik kütüphaneleri manuel kurmak için:")
            for module, pip_name in missing_modules:
                print(f"   pip install {pip_name}")
    
    print_separator()
    
    # Son öneriler
    print("💡 ÖNERİLER:")
    print("1. Sanal ortam kullanmanız tavsiye edilir:")
    print("   python -m venv .venv")
    print("2. Gereksinimleri kaydetmek için:")
    print("   pip freeze > requirements.txt")
    print("3. Tüm gereksinimleri kurmak için:")
    print("   pip install -r requirements.txt")
    
    print_separator()
    print("👨‍💻 Proje: Endüstri 4.0 için AI Destekli Akıllı Üretim Hata Tespiti")
    print("🏫 Kapadokya Üniversitesi - Bilişim Sistemleri ve Teknolojileri")

if __name__ == "__main__":
    main()