# 📘 HappyBooking – Data Engineering Final Projesi

## Microsoft Fabric + Modern Data Stack

Bu doküman, öğrencilerin hem batch hem streaming veri kaynaklarını kullanarak Microsoft Fabric üzerinde Bronze → Silver → Gold mimarisini kurduğu, veri kalite kontrolü, orkestrasyon ve CI/CD gibi gelişmiş kavramları uyguladığı bir Data Engineering projesi oluşturması için hazırlanmıştır.

# 🎬 1. Proje Tanımı

HappyBooking, otel rezervasyon verilerini farklı sistemlerden toplamak istemektedir. Öğrencilerden bu verileri:

- Batch (Kaggle)

- Streaming (Docker → Eventstream)

- API (weather + currency)

şeklinde ingest edip Fabric üzerinde işlenebilir hale getirmesi beklenir.

Amaç:
Bronze → Silver → Gold katmanlı modern veri platformu kurmak ve yönetim için analitik dashboard üretmek.

# 🎯 2. Projenin Amaçları

- Farklı kaynaklardan gelen veriyi ingest etmek (batch + stream + API)

- Veriyi normalize etmek ve temizlemek

- Veri kalitesini doğrulamak

- Gold katmanında iş kuralları oluşturmak

- Power BI ile analiz oluşturmak

- Fabric Workflow + GitHub CI/CD ile modern veri mühendisliği pratiğini uygulamak

# 🧩 3. Kullanılacak Araçlar

- Microsoft Fabric (Lakehouse, Warehouse, Eventstream, Notebook, Workflow, Power BI)

- Docker (stream producer)

- DBT (Gold modelleri)

- Great Expectations (data quality)

- Airflow (DAG → Fabric Pipeline karşılaştırması)

- GitHub Actions (CI/CD)

# 🗂 4. Kullanılacak Veri Setleri
## Batch Veri (Kaggle – Hotel Booking Demand)

- hotel_raw.csv dosyası ikiye bölünecek:

- hotel_raw_batch.csv (%70 – tarihsel batch veri)

- hotel_raw_stream.csv (%30 – gerçek zamanlı simülasyon)

## Streaming Veri (Docker → Eventstream)

- stream_producer.py → satır satır rezervasyon akışı gönderir.

## API Zenginleştirme

- Weather API (Open-Meteo vb.)

- Currency API (ECB / ExchangeRate)

# 🧱 5. Hedef Mimari
Docker Stream Simulator (Python)
        |
        v
Fabric Eventstream  ---> KQL DB (Streaming analytics)
        |
Batch Data (CSV, API)
        |
        v
Fabric Lakehouse (Bronze)
        |
        v
Fabric Notebook (PySpark) + Great Expectations
        |
        v
Fabric Lakehouse (Silver - Cleaned)
        |
        v
DBT (Gold Transformations)
        |
        v
Warehouse / Gold Lakehouse
        |
   +----+----+
   |         |
Power BI   (Opsiyonel Synapse)

# 🗂️ 6. Repo Yapısı
repo-root/
├─ data/
│   ├─ hotel_raw_batch.csv
│   ├─ hotel_raw_stream.csv
├─ docker/
│   ├─ Dockerfile
│   ├─ stream_producer.py
├─ notebooks/
│   ├─ 01_bronze_ingest_batch.py
│   ├─ 02_stream_to_bronze.py
│   ├─ 03_silver_transformations.py
│   ├─ 04_gold_dbt_models/
│   ├─ 05_quality_tests_ge.py
├─ dbt_project/
├─ pipelines/
├─ tests/
├─ .github/workflows/
└─ docs/

# 🔄 7. Proje Adımları (Öğrenci Görevleri)
## ✅ Adım 1 — Batch Verisini Bronze’a Alın

Amaç: Kaggle hotel_raw_batch.csv dosyasını Bronze katmanına ingest etmek.

Yapılacaklar:

- Kaggle’dan veri indirilir.

- hotel_raw.csv → batch + stream olarak ikiye bölünür.

- Bronze’a yazılır (Delta formatı).

- Tarih formatları normalize edilir.

- Dosya versiyonlama yapılır.

## ✅ Adım 2 — Docker Stream Simulator Çalıştırma

Amaç: hotel_raw_stream.csv içindeki kayıtları gerçek zamanlı event olarak Eventstream’e göndermek.

Yapılacaklar:

- Dockerfile ve stream_producer.py incelenir.

- Container ayağa kaldırılır.

- Eventler Eventstream’e akar.

- Flow kontrol edilir.

## ✅ Adım 3 — Streaming Veriyi Bronze’a Yazma

Amaç: Eventstream → Bronze mapping oluşturmak.

Yapılacaklar:

- Eventstream mapping yapılır.

- Auto-create tables açılır.

- Streaming tablosunun oluştuğu doğrulanır.

## ✅ Adım 4 — API Verilerinin Bronze’a Alınması

Amaç: Weather + Currency API verilerini ingest etmek.

Yapılacaklar:

- API çağrıları yapılır.

- JSON → Bronze’a yazılır.

- Tarih & şehir alanları normalize edilir.

## ✅ Adım 5 — Silver Transformations (Temizleme)

Amaç: Bronze içindeki raw veriyi temiz ve analize hazır hale getirmek.

Temizlikler:

- Sadece kritik kolonlarda NULL temizliği

- Duplicate’lerin kaldırılması
  
- Veri Tipi Standardizasyonu

- Tarih formatı standardizasyonu

- Yazım ve Karakter Bozukluklarının Düzeltilmesi

- Mantığa Aykırı Değerlerin Düzeltilmesi / Filtrelenmesi

- Kategorizasyon & Standardizasyon

- Outlier Analizi

## ✅ Adım 6 — Data Quality (Great Expectations)

Amaç: Silver tabakasının kalitesini test etmek.

Testler:

- not_null

- unique

- schema doğrulama

- date format validation

Çıktı: GE raporu (artefact olarak saklanacak)

## ✅ Adım 7 — Gold Katmanı (DBT)

Amaç: İş kuralları & KPI modelleri üretmek.

Modeller:

- fact_booking

- dim_city

- kpi_revenue

Her modelde:

- tests: unique, not_null

- documentation

- lineage graph

## ✅ Adım 8 — Dashboard (Power BI)

Dashboard İçeriği:

- Rezervasyon trendleri

- Şehir bazlı analiz

- Gelir KPI’ları

- KQL DB’den canlı stream grafiği (opsiyonel)

## ✅ Adım 9 — Fabric Workflow Oluşturma & Otomasyon

Amaç: Tüm pipeline adımlarının otomatik çalışması.

Workflow içeriği:

1. Batch ingest notebook

2. Stream mapping kontrol

3. Silver dönüşümleri

4. GE kalite testleri

5. DBT modelleri

6. Warehouse refresh

7. Power BI dataset refresh

Zamanlayıcı: Günlük / saatlik

## ✅ Adım 10 — GitHub Kullanımı & CI/CD

Amaç: Kod versiyonlama + otomasyon.

Yapılacaklar:

- Git repo oluşturulur.

- Fabric notebook’lar Git’e bağlanır.

- Aşağıdaki Workflow oluşturulur:

PR açılınca:

- GE testleri çalışır

- Pytest çalışır

- DBT testleri çalışır

Merge sonrası:

- DBT modelleri CI pipeline’da build edilir

- (Opsiyonel) Fabric REST API ile deploy yapılır

Branch Strategy:

- main → production

- dev → development

# 📊 8. Proje Çıktıları

- Batch + stream + API kaynaklı Bronze verisi

- Silver (temizlenmiş) veri

- Gold (DBT) fact & dimension & KPI tabloları

- GE kalite raporu

- Power BI dashboard

- Workflow + GitHub Actions CI/CD

- Docker stream simulator

# 📦 9. Beklenen Sonuç

Öğrenci proje sonunda:

- Modern veri mühendisliği mimarisini uçtan uca kurmuş olur.

- Batch + streaming entegrasyonunu anlar.

- Data Quality, DBT, Workflow, CI/CD gibi ileri seviye kavramlarda uygulama yapar.

- Microsoft Fabric'i gerçek bir senaryoda deneyimler.



<img width="4068" height="1760" alt="happybooking_architecture_white" src="https://github.com/user-attachments/assets/fd96d38c-e2c8-4d74-b169-a0cbc964c2dd" />
