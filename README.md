# PokeFinder

**PokeFinder**, Pokémon'ların detaylı bilgilerini (isim, türler, yetenekler, boy, ağırlık) PokéAPI kullanarak çeken ve kullanıcıya sunan bir Python uygulamasıdır. Hem terminal tabanlı hem de GUI tabanlı bir versiyonu vardır.

---

## 🚀 Özellikler

- **Pokémon Bilgisi Çekme**: Kullanıcının istediği Pokémon’un boyunu, ağırlığını, türlerini ve yeteneklerini listeler.
- **Kullanıcı Dostu Arayüz**: Tkinter ile oluşturulmuş basit bir GUI arayüzü.
- **PokéAPI Kullanımı**: Gerçek zamanlı API istekleri ile veri çekme.

---

## 📂 Proje Yapısı

```plaintext
PokeFinder/
├── main.py             # Ana Python dosyası (GUI versiyonu)
├── README.md           # Proje açıklamaları
├── requirements.txt    # Gerekli Python paketleri
```

---

## 🔧 Kurulum ve Çalıştırma

### 1. Gerekli Bağımlılıkları Yükleyin
Proje dizininde aşağıdaki komutu çalıştırarak gerekli Python kütüphanelerini yükleyin:
```bash
pip install -r requirements.txt
```

### 2. Uygulamayı Çalıştırın
Proje dizininde aşağıdaki komutu kullanarak GUI uygulamasını başlatabilirsiniz:
```bash
python main.py
```

---

## 📜 Kullanım

### Terminal Versiyonu
- Kullanıcıdan Pokémon adı alınır ve API'den çekilen bilgiler terminalde görüntülenir.

### GUI Versiyonu
1. Uygulama başlatıldığında bir giriş kutusu ve bir arama butonu ile karşılaşırsınız.
2. Pokémon adını girip **Ara** butonuna tıkladığınızda:
   - Pokémon’un bilgileri ekranda görüntülenir.
3. Eğer Pokémon bulunamazsa, bir hata mesajı görüntülenir.

---

## 🌟 Geliştirme Önerileri

1. **Fotoğraf Gösterimi**:
   - Pokémon’un fotoğrafını, API’den çekilen "sprites" verisiyle GUI’ye ekleyebilirsiniz.

2. **Çoklu Pokémon Arama**:
   - Birden fazla Pokémon’un detaylarını aynı anda listeleyebilme özelliği ekleyebilirsiniz.

3. **JSON/CSV Kaydetme**:
   - Çekilen Pokémon verilerini bir dosyaya (JSON veya CSV) kaydetme özelliği eklenebilir.

4. **Türlere Göre Filtreleme**:
   - Belirli bir Pokémon türüne göre arama yapma (örneğin: "fire", "water").

5. **Asenkron API İstekleri**:
   - `asyncio` ve `aiohttp` kullanarak API isteklerini hızlandırabilirsiniz.

---

## 💻 Örnek Kullanım

### **Girdi**:
Pokémon adını girin: `pikachu`

### **Çıktı** (GUI'de veya terminalde):
```plaintext
Ad: pikachu
Boy: 4 dm
Ağırlık: 60 hg
Tipler: electric
Yetenekler: static, lightning-rod
```

---

## 🔑 PokéAPI Hakkında

- **PokéAPI** ([https://pokeapi.co/](https://pokeapi.co/)), Pokémon verilerini sunan ücretsiz bir API'dir.
- Bu uygulama, PokéAPI'nin sağladığı JSON verilerini çekmek ve işlemek için `requests` modülünü kullanır.

---

## 🛠️ Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

---

## ✨ İletişim

Herhangi bir soru veya öneriniz varsa, lütfen [sabuncumustafasait@gmail.com](mailto:your_email@example.com) adresinden iletişime geçin.
```
