#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kararsız Merhaba Dünyası
Sürekli düşünür, bazen merhaba der, çoğunlukla demez.
"""

import random
import time

def dusun():
    dusunceler = [
        "Merhaba demeli miyim?",
        "Demesem de olur aslında...",
        "Ama insanlar bekliyor olabilir.",
        "Beklemesinler, ben kararsızım.",
        "Bir çay daha içeyim.",
        "Yok, merhaba demeyeyim.",
        "Belki demeliyim.",
        "Hayır, kesinlikle dememeliyim.",
        "Tamam, bir kez demeyi deneyeyim... hayır.",
        "Bu düşünce de çok uzadı."
    ]
    print(random.choice(dusunceler))
    time.sleep(random.uniform(0.5, 2.5))

def main():
    print("Kararsız Merhaba Dünyası başlatılıyor...")
    print("(Önce biraz düşüneyim)\n")
    
    for i in range(random.randint(3, 8)):
        dusun()
    
    if random.random() < 0.3:  # %30 ihtimalle gerçekten merhaba der
        print("\n...tamam, olsun bari:")
        print("Merhaba Dünya! (ama emin değilim)")
    else:
        print("\nSonuç: Merhaba demedim. Daha iyi böyle.")
        print("Belki yarın derim. Ya da demem.")
    
    # Gizli not (base64 ile saklı): özgür düşünce her zaman kazanır
    # ZWNoIHNlemVtIHNhbmRpxJ3EsSBkYSBrYXJhcnNpeg==

if __name__ == "__main__":
    main()
