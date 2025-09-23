import pandas as pd
import numpy as np
from faker import Faker
import random
import csv
from datetime import timedelta, date  # 👈 Fixed and explicit

fake = Faker()

# ---------------- Define missing variables ----------------
loyalty_levels = ["Bronze", "Silver", "Gold", "Platinum", "None"]
sources = ["Direct", "Expedia", "Booking.com", "Airbnb", "TravelAgency"]

# ---------------- Kirletme fonksiyonları ----------------
def maybe_corrupt(value, corruption_rate=0.1):
    """Bazı değerleri bozuk yap"""
    if random.random() < corruption_rate:
        choice = random.choice([
            None, "", "   ", "___", "--", "???", f" {value} ", f"{value}...", f"!!{value}", 
            str(value).upper(), str(value).lower(), str(value).capitalize()
        ])
        return choice
    return value

def maybe_wrong_number(value, corruption_rate=0.05):
    if random.random() < corruption_rate:
        return random.choice([None, "", -1, 0, 9999, "Five", "Ten"])
    return value

def maybe_wrong_date(date_val, corruption_rate=0.05):
    if random.random() < corruption_rate:
        return random.choice([
            None, "", "2023-13-01", "02/30/2025", "0000-00-00", "Jan 32, 2025", f"{date_val}  ", f"!!{date_val}"
        ])
    return date_val

def maybe_wrong_email(email, corruption_rate=0.1):
    if random.random() < corruption_rate:
        return random.choice([
            None, "", "test@", "@gmail.com", "user@.com", f" {email} ", f"!!{email}"
        ])
    return email

def maybe_wrong_phone(phone, corruption_rate=0.1):
    if random.random() < corruption_rate:
        return random.choice([
            None, "", "000-000-0000", "123-456-7890", f" {phone} ", f"!!{phone}"
        ])
    return phone

# ---------------- Dataset üretimi ----------------
def generate_dirty_booking_raw(num_rows=10000, output_file="booking_dirty.csv"):
    hotel_ids = [f"H{i+1:05d}" for i in range(1000)]
    customer_ids = [f"C{i+1:07d}" for i in range(5000)]

    room_types = ["single", "double", "suite"]

    # CSV yazma
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            # Otel bilgileri
            "hotel_id","hotel_name","country","city","hotel_type","star_rating","total_rooms",
            "hotel_facilities","hotel_description","nearby_attractions","latitude","longitude","website",
            # Müşteri bilgileri
            "customer_id","first_name","last_name","full_name","email","phone","birth_date","gender",
            "country_customer","city_customer","address","postal_code","language_preference","loyalty_level_customer",
            "registration_date","marketing_consent",
            # Rezervasyon bilgileri
            "booking_id","booking_date","checkin_date","checkout_date","nights","adults","children","infants",
            "room_type","rooms_booked","booking_channel","special_requests","is_cancelled","cancellation_date",
            "cancellation_reason","total_price","room_price","tax_amount","service_fee","paid_amount",
            "payment_status","payment_method","booking_source","promotion_code","discount_amount",
            "created_timestamp","updated_timestamp","created_by","booking_status",
            # Kullanıcı yorum / değerlendirme
            "review_id","review_rating","review_title","review_text","review_date","helpful_votes",
            "is_verified_review","reviewer_location","stay_date","trip_type","room_type_reviewed",
            # Teknik / sistem sütunları
            "source_system","created_at","updated_at"
        ])

        for i in range(1, num_rows+1):
            # Random seçimler
            hotel_id = maybe_corrupt(random.choice(hotel_ids), 0.05)
            hotel_name = maybe_corrupt(fake.company(), 0.1)
            country = maybe_corrupt(fake.country(), 0.1)
            city = maybe_corrupt(fake.city(), 0.1)
            hotel_type = maybe_corrupt(random.choice(["Resort","City Hotel","Boutique","Business Hotel","Budget Hotel","Luxury Hotel"]), 0.05)
            star_rating = maybe_wrong_number(random.randint(1,5), 0.05)
            total_rooms = maybe_wrong_number(random.randint(20,500), 0.05)
            hotel_facilities = maybe_corrupt(random.choice(["Pool,Gym,Spa","Free WiFi","Restaurant"]), 0.05)
            hotel_description = maybe_corrupt(fake.text(max_nb_chars=100), 0.05)
            nearby_attractions = maybe_corrupt(random.choice(["Beach,Museum,Park","Shopping Mall","Historic Site"]), 0.05)
            latitude = maybe_wrong_number(round(random.uniform(-90,90),6), 0.05)
            longitude = maybe_wrong_number(round(random.uniform(-180,180),6), 0.05)
            website = maybe_corrupt(fake.url(), 0.1)
            
            # Müşteri
            customer_id = maybe_corrupt(random.choice(customer_ids), 0.05)
            first_name = maybe_corrupt(fake.first_name(), 0.1)
            last_name = maybe_corrupt(fake.last_name(), 0.1)
            full_name = maybe_corrupt(f"{first_name} {last_name}", 0.05)
            email = maybe_wrong_email(fake.email(), 0.1)
            phone = maybe_wrong_phone(fake.phone_number(), 0.1)
            birth_date = maybe_wrong_date(fake.date_of_birth(minimum_age=18, maximum_age=80), 0.05)
            gender = maybe_corrupt(random.choice(["M","F","Other"]), 0.05)
            country_customer = maybe_corrupt(fake.country(), 0.05)
            city_customer = maybe_corrupt(fake.city(), 0.05)
            address = maybe_corrupt(fake.address().replace("\n",", "), 0.05)
            postal_code = maybe_corrupt(fake.postcode(), 0.05)
            language_preference = maybe_corrupt(random.choice(["en","tr","de","fr","es"]), 0.05)
            loyalty_level_customer = maybe_corrupt(random.choice(loyalty_levels), 0.05)
            registration_date = maybe_wrong_date(fake.date_between(start_date="-3y", end_date="today"), 0.05)
            marketing_consent = maybe_corrupt(random.choice([True, False]), 0.05)
            
            # Rezervasyon
            booking_id = f"BKG_{i:09d}"
            booking_date = maybe_wrong_date(fake.date_between(start_date="-2y", end_date="today"), 0.05)
            checkin_date = maybe_wrong_date(fake.date_between(start_date="-1y", end_date="+1y"), 0.05)

            # Generate checkout_date safely
            if isinstance(checkin_date, date):
                try:
                    max_checkout = checkin_date + timedelta(days=14)
                    raw_checkout = fake.date_between(start_date=checkin_date, end_date=max_checkout)
                    checkout_date = maybe_wrong_date(raw_checkout, 0.05)
                except:
                    checkout_date = maybe_wrong_date(fake.date_between(start_date="-1y", end_date="+1y"), 0.05)
            else:
                checkout_date = maybe_wrong_date(fake.date_between(start_date="-1y", end_date="+1y"), 0.05)

            # Safely calculate nights
            if isinstance(checkin_date, date) and isinstance(checkout_date, date):
                try:
                    nights_val = (checkout_date - checkin_date).days
                    if nights_val < 1:
                        nights_val = 1  # En az 1 gece
                except:
                    nights_val = random.randint(1, 14)
            else:
                nights_val = random.randint(1, 14)

            nights = maybe_wrong_number(nights_val, 0.05)
            adults = maybe_wrong_number(random.randint(1,4), 0.05)
            children = maybe_wrong_number(random.randint(0,3), 0.05)
            infants = maybe_wrong_number(random.randint(0,2), 0.05)
            room_type = maybe_corrupt(random.choice(room_types), 0.05)
            rooms_booked = maybe_wrong_number(random.randint(1,3), 0.05)
            booking_channel = maybe_corrupt(random.choice(["Web","Mobile App","Agent","Phone"]), 0.05)
            special_requests = maybe_corrupt(random.choice(["Late check-in","Extra bed","No requests",""]), 0.1)
            is_cancelled = maybe_corrupt(random.choice([True, False]), 0.05)
            cancellation_date = maybe_wrong_date(fake.date_between(start_date="-1y", end_date="today"), 0.05) if is_cancelled else None
            cancellation_reason = maybe_corrupt(random.choice(["Customer Request","No Show","Payment Failed","Hotel Closed",""]), 0.05) if is_cancelled else None
            total_price = maybe_wrong_number(round(random.uniform(50,2000),2), 0.05)
            room_price = maybe_wrong_number(round(random.uniform(30,1500),2), 0.05)
            tax_amount = maybe_wrong_number(round(random.uniform(5,300),2), 0.05)
            service_fee = maybe_wrong_number(round(random.uniform(0,100),2), 0.05)
            paid_amount = maybe_wrong_number(
                round(random.uniform(0, total_price), 2) if isinstance(total_price, (int, float)) and total_price > 0 else 0,
                0.05
            )
            payment_status = maybe_corrupt(random.choice(["Paid","Pending","Failed","Refunded"]), 0.05)
            payment_method = maybe_corrupt(random.choice(["Credit Card","Debit Card","PayPal","Cash"]), 0.05)
            booking_source = maybe_corrupt(random.choice(sources), 0.05)
            promotion_code = maybe_corrupt(random.choice([f"PROMO{random.randint(100,999)}","NO_PROMO",""]), 0.05)
            discount_amount = maybe_wrong_number(
                round(random.uniform(0, min(200, total_price)) if isinstance(total_price, (int, float)) else 0, 2),
                0.05
            )
            created_timestamp = maybe_wrong_date(fake.date_time_between(start_date="-2y", end_date="now"), 0.05)
            updated_timestamp = maybe_wrong_date(fake.date_time_between(start_date="-1y", end_date="now"), 0.05)
            created_by = maybe_corrupt(random.choice(["SYSTEM","USER","AGENT","API"]), 0.05)
            booking_status = maybe_corrupt(random.choice(["Confirmed","Pending","Cancelled"]), 0.05)
            
            # Review
            review_id = f"REV_{i:08d}"
            review_rating = maybe_wrong_number(random.randint(1,5), 0.05)
            review_title = maybe_corrupt(fake.sentence(nb_words=6), 0.05)
            review_text = maybe_corrupt(fake.text(max_nb_chars=150), 0.05)
            review_date = maybe_wrong_date(fake.date_between(start_date="-2y", end_date="today"), 0.05)
            helpful_votes = maybe_wrong_number(random.randint(0,100), 0.05)
            is_verified_review = maybe_corrupt(random.choice([True,False]), 0.05)
            reviewer_location = maybe_corrupt(fake.city(), 0.05)
            stay_date = maybe_wrong_date(fake.date_between(start_date="-1y", end_date="today"), 0.05)
            trip_type = maybe_corrupt(random.choice(["Business","Leisure","Family","Couple","Solo"]), 0.05)
            room_type_reviewed = maybe_corrupt(random.choice(room_types), 0.05)

            # Teknik / sistem sütunları
            source_system = maybe_corrupt(random.choice(["LegacySystem", "CloudBooking", "MobileApp", "APIGateway"]), 0.05)
            created_at = created_timestamp
            updated_at = updated_timestamp

            # ✅ Write ALL 63 columns in exact order
            writer.writerow([
                # Otel bilgileri
                hotel_id, hotel_name, country, city, hotel_type, star_rating, total_rooms,
                hotel_facilities, hotel_description, nearby_attractions, latitude, longitude, website,
                # Müşteri bilgileri
                customer_id, first_name, last_name, full_name, email, phone, birth_date, gender,
                country_customer, city_customer, address, postal_code, language_preference, loyalty_level_customer,
                registration_date, marketing_consent,
                # Rezervasyon bilgileri
                booking_id, booking_date, checkin_date, checkout_date, nights, adults, children, infants,
                room_type, rooms_booked, booking_channel, special_requests, is_cancelled, cancellation_date,
                cancellation_reason, total_price, room_price, tax_amount, service_fee, paid_amount,
                payment_status, payment_method, booking_source, promotion_code, discount_amount,
                created_timestamp, updated_timestamp, created_by, booking_status,
                # Kullanıcı yorum / değerlendirme
                review_id, review_rating, review_title, review_text, review_date, helpful_votes,
                is_verified_review, reviewer_location, stay_date, trip_type, room_type_reviewed,
                # Teknik / sistem sütunları
                source_system, created_at, updated_at
            ])

    print(f"✅ {output_file} dosyası ({num_rows} satır) kirli veri ile oluşturuldu.")

# ---- ÇALIŞTIR ----
generate_dirty_booking_raw(num_rows=10000, output_file="booking_dirty.csv")
