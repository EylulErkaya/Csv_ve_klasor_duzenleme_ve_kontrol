import os
from collections import defaultdict

def klasor_png_sayilari_ve_yollari(root_dir):
    png_klasorleri = defaultdict(list)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        png_sayisi = sum(1 for file in filenames if file.lower().endswith('.png'))
        if 1 <= png_sayisi <= 8:
            png_klasorleri[png_sayisi].append(dirpath)

    return png_klasorleri

# Ana dizin yolu
ana_klasor = "D:\\cropped_images"

# Veriyi al
klasorler_dict = klasor_png_sayilari_ve_yollari(ana_klasor)

# 1'den 5'e kadar listele
for i in range(1, 5):
    klasorler = klasorler_dict.get(i, [])
    print(f"\n{i} tane .png içeren {len(klasorler)} klasör bulundu.")
    for klasor in klasorler:
        print("   -", klasor)
