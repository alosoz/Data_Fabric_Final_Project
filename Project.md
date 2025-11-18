# 🎯 Gorevler 

1. Docker (Stream Simulator) – canlı rezervasyon olaylarını üretmek için.

2. DBT (Gold Transformations) – KPI tablolarını modellemek için.

3. Great Expectations (Data Quality) – Silver/Gold katmanında veri testleri için.
 

- Airflow (DAG vs Fabric Pipeline) – orkestrasyon karşılaştırması.

- GitHub Actions (CI/CD) – pipeline & notebook versiyon kontrolü.

---

# 🏨 Booking.com Esinli Data Engineering Projesi (Fabric + Advanced Tools)
##📌 Proje Amacı

HappyBooking, otel rezervasyon verilerini batch + stream olarak toplamak ve bunları Microsoft Fabric üzerinde işleyerek analitik dashboard’lar üretmek istiyor.

Bu projede öğrenciler, gerçek dünyaya yakın bir senaryoda:

- Bronze–Silver–Gold (Delta Lake) mimarisi

- Streaming + Batch entegrasyonu

- Veri kalite, orkestrasyon, CI/CD gibi modern uygulamalar

ile uçtan uca bir Data Engineering Pipeline geliştirecek.

---

# ✅ Başarı Ölçütleri

- Uçtan uca pipeline çalışır (batch + stream).

- Docker stream simulator doğru şekilde Eventstream’e veri gönderir.

- DBT modelleri Gold tabakasında KPI tablolarını üretir.

- Great Expectations testleri veri kalitesini garanti eder.
 

- Airflow DAG ile Fabric Pipeline karşılaştırması yapılır. 

- GitHub Actions ile CI/CD uygulanır. 

- Power BI dashboard ile analizler tamamlanır.

---

# 🎯 Projeden Ne Bekleniyor?

##Teknik Hedefler

- Microsoft Fabric servislerini kullanarak batch + streaming pipeline kurmak.

- Bronze → Silver → Gold dönüşümlerini PySpark + DBT ile uygulamak.

- Veri kalitesini Great Expectations ile doğrulamak.

- Docker tabanlı stream generator çalıştırmak.

- Opsiyonel: Airflow & GitHub Actions entegrasyonu.

##Başarı Kriterleri

- Katmanlı mimari eksiksiz çalışmalı.

- Data Quality testleri %100 geçmeli.

- Power BI dashboard’ları KPI’ları göstermeli.

- Kod ve pipeline’lar versiyon kontrolünde olmalı.

---

# 🗂️ Veri Setleri

- Batch: Hotel Booking Demand (Kaggle) + TripAdvisor Reviews.

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

- Stream: Docker içinde çalışan Python script → Eventstream.

Docker Stream Simulator ile Streaming Verisi Üretme

  Amaç: hotel_raw_stream.csv dosyasını gerçek zamanlı bir rezervasyon akışı gibi Eventstream’e göndermek.

Yapılacaklar

Docker klasöründeki Dockerfile ve stream_producer.py dosyalarını inceleyin.

Container’ı başlatın.

Script, hotel_raw_stream.csv verisini satır satır Eventstream’e gönderecek.

Eventstream üzerindeki data flow’u kontrol edin.

Eventstream’den Streaming Verisini Bronze’a Yazma

Amaç: Eventstream’den gelen canlı veriyi Bronze tabakasına kaydetmek.

Yapılacaklar

Eventstream → Lakehouse mapping oluşturun.

Auto-create table özelliğini aktif edin.

Streaming tablosunun Bronze’ta oluştuğunu doğrulayın.

- Zenginleştirme: World Cities, Weather snapshot, kur bilgileri.

  API Verilerinin Bronze’a Alınması (Weather + Currency)

Amaç: Zenginleştirme için harici API verilerini projeye dahil etmek.

Yapılacaklar

Ücretsiz API’lerden veri çekilecek:

Weather API (Open-Meteo vb.)

Currency API (ExchangeRate API veya ECB RSS)

API verilerini Bronze’a kaydedin.

Tarih & şehir kolonlarını normalize edin.

---

🏗️ Hedef Mimari
Docker Stream Simulator (Python)
        |
        v
Fabric Eventstream  ---> KQL DB (streaming analytics)
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
Fabric Lakehouse (Silver - Cleaned)
        |
        v
DBT Models (Gold Transformations)
        |
        v
Fabric Warehouse / Gold Lakehouse
        |
   +----+----+
   |         |
Power BI   Synapse (opsiyonel query layer)

---

# ☁️ Kullanılacak Servis & Tool’lar

## Microsoft Fabric İçinde

- Lakehouse / OneLake – Batch & streaming depolama

- Eventstream – Stream ingest

- KQL DB – Streaming analytics

- Notebook (PySpark) – Transformation + Data Quality integration

- Warehouse – SQL tabanlı business layer

- Power BI – Dashboard

## Ek Zorunlu Tool’lar

- Docker – Stream simulator

- DBT – Gold layer transformations (fact_booking, dim_city, KPI hesaplama)

- Great Expectations – Data Quality testleri (Null, duplicate, schema)
 

- Airflow – Orkestrasyon (Fabric Pipeline alternatifi)

- GitHub Actions – CI/CD (Notebook + Pipeline JSON deployment)

---

# 📁 Repo Yapısı
repo-root/
├─ infrastructure/ (IaC, opsiyonel)
├─ data/ (örnek CSV)
├─ docker/ (stream simulator)
│   ├─ Dockerfile
│   ├─ stream_producer.py
├─ notebooks/
│   ├─ 01_bronze_ingest_batch.py
│   ├─ 02_stream_to_bronze.py
│   ├─ 03_silver_transformations.py
│   ├─ 04_gold_dbt_models/
│   │   ├─ fact_booking.sql
│   │   ├─ dim_city.sql
│   │   ├─ kpi_revenue.sql
│   └─ 05_quality_tests_ge.py
├─ dbt_project/ (DBT configs & models)
├─ pipelines/ (Fabric pipeline JSON + opsiyonel Airflow DAGs)
├─ tests/ (great_expectations, pytest)
├─ .github/workflows/ (opsiyonel CI/CD)
└─ docs/ (readme, runbooks, diagrams)

---

# 🔄 Adımlar

1. Batch Ingestion (Fabric) – CSV/JSON verilerini Bronze’a al.

2. Stream Simulator (Docker) – Eventstream’e canlı veri gönder.

3. Bronze → Silver (PySpark) – Temizleme, normalize etme.

4. Data Quality (Great Expectations) – Silver verilerini test et.

5. Silver → Gold (DBT) – Fact/dim tablolar, KPI hesaplamaları.

6. Warehouse + Power BI – Dashboard hazırlama.

7. Airflow DAG vs Fabric Pipeline karşılaştırması. 

8. - GitHub Actions ile CI/CD. 

---

# 📊 Çıktılar

- Çalışan Docker simulator (stream).

- Bronze, Silver, Gold katman tabloları.

- DBT modelleri ve çalıştırma çıktıları.

- Great Expectations raporları.

- Power BI dashboard:

  - Rezervasyon sayısı (trend, şehir bazlı)

  - İptal oranı

  - Gelir KPI’ları

  - Streaming trendleri (KQL DB’den)

---

# 📦 Beklenen Sonuç

- Uçtan uca çalışan Fabric Data Engineering Pipeline.

- Gerçek zamanlı + batch veri entegrasyonu.

- Modern data stack tecrübeleri: Docker, DBT, Data Quality.

- Opsiyonel olarak orkestrasyon & CI/CD yetkinliği.
