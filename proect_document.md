# Happybooking Project
📘 HappyBooking – Data Engineering Final Projesi Dokümanı

Bu doküman, öğrencilerin Microsoft Fabric + Modern Data Stack kullanarak uçtan uca bir veri mühendisliği projesi geliştirmeleri için hazırlanmıştır. Projede batch ve streaming veriyi bir arada işleyen, veri kalitesini doğrulayan ve yönetim için analitik dashboard üreten bir yapı kurulacaktır.

🎬 1. Proje Tanımı

HappyBooking, farklı kaynaklardan gelen otel rezervasyon verilerini toplayıp düzenleyerek analitik raporlar oluşturmak isteyen bir turizm şirketidir. Şirket sizden operasyonel verileri Bronze → Silver → Gold katmanlarında işleyen uçtan uca bir Data Engineering Pipeline tasarlamanızı ister.

🎯 2. Projenin Amaçları

Farklı veri kaynaklarından (dosya, API, stream) gelen veriyi toplamak.

Gelen veriyi temizlemek, standartlaştırmak ve işlemek.

Final veriyi yönetime sunulacak dashboard’larda kullanılacak hale getirmek.

Modern Data Engineering araçlarını gerçekçi bir senaryoda uygulamak.

🧩 3. Kullanılacak Araçlar
✔️ Zorunlu Araçlar

Docker – Stream simulator çalıştırmak için.

Microsoft Fabric

Eventstream (stream ingest)

Lakehouse (Bronze–Silver–Gold)

Notebook (PySpark)

Warehouse (SQL layer)

Power BI

DBT – Gold katmanı ve KPI tabloları için.

Great Expectations – Data Quality testleri için.

➕ İsteğe Bağlı Araçlar

Airflow – Orkestrasyon karşılaştırması.

GitHub Actions – CI/CD süreçleri.

🧱 4. Mimari Genel Bakış

Aşağıdaki yapı uçtan uca proje mimarisini gösterir:

Docker Stream Simulator (Python)
        |
        v
Fabric Eventstream  ---> KQL DB (stream analytics)
        |
Batch Data (CSV, JSON, API)
        |
        v
Fabric Lakehouse (Bronze)
        |
        v
Fabric Notebook (PySpark) + Great Expectations
        |
        v
Fabric Lakehouse (Silver)
        |
        v
DBT Models (Gold Transformations)
        |
        v
Warehouse / Gold Lakehouse
        |
   +----+----+
   |         |
Power BI   (Opsiyonel Synapse)
📁 5. Repo Yapısı
repo-root/
├─ data/
├─ docker/
│   ├─ Dockerfile
│   ├─ stream_producer.py
├─ notebooks/
│   ├─ 01_bronze_ingest_batch.py
│   ├─ 02_stream_ingest.py
│   ├─ 03_silver_transformations.py
│   ├─ 04_gold_dbt_models/
│   ├─ 05_quality_tests_ge.py
├─ dbt_project/
├─ pipelines/
├─ tests/
├─ .github/workflows/ (opsiyonel)
└─ docs/
🔄 6. Proje Adımları (Öğrenci Görevleri)

Aşağıdaki bölümler proje boyunca öğrencilerin takip edeceği adımları açıklar.

✅ Adım 1 — Batch Verisini Bronze Katmanına Alın

Amaç: CSV/JSON verilerini Fabric Lakehouse Bronze alanına aktarmak.

Yapılacaklar

Kaggle hotel booking dataset → Bronze'a ingest

Tarih formatlarını kontrol etme

Kaynak dosyaları versionlama

Notebook içerisinde Delta formatına yazma

✅ Adım 2 — Docker Stream Simulator Çalıştırma

Amaç: Gerçek zamanlı rezervasyon olayları üretmek.

Yapılacaklar

Dockerfile ve producer script inceleme

Container’ı ayağa kaldırma

Eventler → Eventstream’e aktarılacak

Eventstream üzerindeki flow kontrol edilecek

✅ Adım 3 — Streaming Veriyi Bronze’a Yazma

Amaç: Eventstream’den gelen live event’leri Bronze tabakasına kaydetmek.

Yapılacaklar

Eventstream → Lakehouse Mapping

Auto-create tables özelliği

Streaming tablo yapısının test edilmesi

✅ Adım 4 — Silver Transformations (Temizleme)

Amaç: Bronze’daki raw veriyi temizlemek ve normalize etmek.

Silver'da Yapılacak Temizlikler

Null cleaning (yalnızca kritik kolonlar)

Duplicate kayıtların kaldırılması

Tarih formatlarının standardize edilmesi

Veri tiplerinin düzeltilmesi

PySpark notebook içinde yapılır.

✅ Adım 5 — Data Quality (Great Expectations)

Amaç: Silver tabakasının kalite testlerini yapmak.

Test Örnekleri

Kolon boşluk kontrolü

Tarih formatı kontrolü

Primary key duplicate testi

Schema doğrulaması

Test raporları proje çıktısı olarak istenecektir.

✅ Adım 6 — Gold Katmanı (DBT Modelleri)

Amaç: İş kurallarının uygulanması ve KPI tablolarının oluşturulması.

DBT’de Oluşturulacak Modeller

fact_booking – temel rezervasyon tablosu

dim_city – şehir boyutu

kpi_revenue – gelir KPI hesaplamaları

Beklenenler

Model ilişkileri

Testler (unique, not_null)

Dokumentasyon

✅ Adım 7 — Dashboard: Power BI

Amaç: İş birimine sunulacak analizler oluşturmak.

Dashboard İçeriği

Rezervasyon sayısı trendi

Şehir bazlı dağılım

Gelir analizleri

Canlı veri akışı grafikleri (opsiyonel: KQL DB)

📝 7. Proje Teslimi

Öğrencilerden aşağıdakiler teslim edilecektir:

Çalışan pipeline (stream + batch)

Bronze / Silver / Gold tabloları

DBT modelleri ve test raporları

Great Expectations kalite raporları

Power BI dosyası

📦 8. Beklenen Sonuç

Bu projenin sonunda öğrenciler:

Uçtan uca modern bir data engineering çözümü kurmuş olacak,

Fabric, DBT, Docker, GE gibi araçları gerçek bir senaryoda uygulayacak,

Streaming + batch entegrasyonunu deneyimleyecek,

Veri kalitesi ve business modeling tecrübesi kazanacaktır.

Hazırlayan: Eğitmen

Bu doküman proje boyunca öğrencilerin referans olarak kullanması içindir.

🔄 Güncellenmiş Proje Adımları (Batch + Stream + API)

Aşağıdaki adımlar yeni veri düzenine göre oluşturulmuştur. Batch, streaming ve API kaynakları net ayrılmıştır.

✅ Adım 1 — Batch Verisinin Bronze Katmanına Alınması

Amaç: Kaggle’dan indirilen hotel_raw.csv dosyasının geçmiş verilere karşılık gelen kısmını Bronze’a aktarmak.

Yapılacaklar

Kaggle’dan hotel_raw.csv dosyasını indirin.

Veriyi ikiye ayırın:

hotel_raw_batch.csv → geçmiş batch veri (%70 önerilir)

hotel_raw_stream.csv → streaming için kullanılacak kısmı (%30 önerilir)

hotel_raw_batch.csv dosyasını Notebook ile Bronze Lakehouse katmanına ingest edin.

Tarih formatlarını normalleştirin.

Veri kaynak dosyalarını versiyonlayın.

Bronze’a Delta formatında yazın.

✅ Adım 2 — Docker Stream Simulator ile Streaming Verisi Üretme

Amaç: hotel_raw_stream.csv dosyasını gerçek zamanlı bir rezervasyon akışı gibi Eventstream’e göndermek.

Yapılacaklar

Docker klasöründeki Dockerfile ve stream_producer.py dosyalarını inceleyin.

Container’ı başlatın.

Script, hotel_raw_stream.csv verisini satır satır Eventstream’e gönderecek.

Eventstream üzerindeki data flow’u kontrol edin.

✅ Adım 3 — Eventstream’den Streaming Verisini Bronze’a Yazma

Amaç: Eventstream’den gelen canlı veriyi Bronze tabakasına kaydetmek.

Yapılacaklar

Eventstream → Lakehouse mapping oluşturun.

Auto-create table özelliğini aktif edin.

Streaming tablosunun Bronze’ta oluştuğunu doğrulayın.

✅ Adım 4 — API Verilerinin Bronze’a Alınması (Weather + Currency)

Amaç: Zenginleştirme için harici API verilerini projeye dahil etmek.

Yapılacaklar

Ücretsiz API’lerden veri çekilecek:

Weather API (Open-Meteo vb.)

Currency API (ExchangeRate API veya ECB RSS)

API verilerini Bronze’a kaydedin.

Tarih & şehir kolonlarını normalize edin.

Güncellenmiş proje adımlarını dokümana başarıyla ekledim!
İstersen:

✅ Öğrenciler için ayrı görev listesi (assignment sheet)
✅ Öğretmen için değerlendirme rubriği
✅ Öğrencilerin dolduracağı proje teslim template’i
✅ Docker stream simulator için hazır script
✅ Weather & currency API çağrıları için örnek kod
