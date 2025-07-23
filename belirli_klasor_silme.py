import os
import shutil
import pandas as pd

def klasorleri_bul_kacinci_png_1_olanlar(root_dir):
    klasorler = []

    for dirpath, dirnames, filenames in os.walk(root_dir):
        png_sayisi = sum(1 for file in filenames if file.lower().endswith('.png'))
        if png_sayisi == 1:
            klasorler.append(dirpath)

    return klasorler

# Kullanıcıdan gelen ayarlar
ana_klasor = "D:\\cropped_images"  # Ana klasör yolu
csv_dosyasi = "dicom_metadata.csv"        # Mevcut CSV dosyasının adı
csv_klasor_sutun_adi = "Directory_Path"  # CSV'de klasör yolu olan sütunun adı

# 1 adet PNG içeren klasörleri bul
silinecek_klasorler = klasorleri_bul_kacinci_png_1_olanlar(ana_klasor)

# Klasörleri sil
for klasor in silinecek_klasorler:
    try:
        shutil.rmtree(klasor)
        print(f"Silindi: {klasor}")
    except Exception as e:
        print(f"Silinemedi: {klasor} - {e}")

# CSV'den bu klasörleri çıkar
df = pd.read_csv(csv_dosyasi)

# Filtrele: bu klasörlerin olduğu satırları çıkar
df_filtered = df[~df[csv_klasor_sutun_adi].isin(silinecek_klasorler)]

# CSV'yi güncelle (aynı dosyaya overwrite)
df_filtered.to_csv(csv_dosyasi, index=False)

print(f"\nToplam {len(silinecek_klasorler)} klasör silindi ve CSV güncellendi.")
