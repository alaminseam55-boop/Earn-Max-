import random
import time
import requests

BOT_TOKEN = "8664893118:AAGzEUGWu3rskerlKk4v8N42sBlXFIMRFAg"
CHAT_ID = "-1003991792277"
IMAGE_URL = "https://i.postimg.cc/N02NLhCD/1790476363225.jpg"

raw_names = """
Ayaan
Zayan
Aryan
Rayyan
Arham
Samaira
Kabir
Aarav
Rohan
Reyansh
Shaan
Vivaan
Zaid
Farhan
Rehan
Aariz
Arman
Nihan
Shayan
Izaan
Adyan
Faheem
Tahsin
Rizwan
Zubair
Kian
Hamza
Taimur
Bilal
Ahad
Daniyal
Sameer
Nabeel
Zidan
Rayan
Sarah
Mirza
Eshan
Safwan
Wasif
Ahil
Nahian
Zohan
Tanvir
Sami
Nahid
Afnan
Armaan
Irfan
Mahir
Tawhid
Zeeshan
Rafi
Rifat
Anas
Hasin
Sayed
Junaid
Riyad
Ivaan
Siyam
Rayid
Muntaha
Parvez
Ashik
Shahil
Aarush
Tamim
Aman
Affan
Yusuf
Ayan
Naeem
Nafis
Rakin
Shahid
Zuhayr
Adil
Ehan
Munim
Raad
Tashfin
Nihal
Rizvi
Sadman
Shafin
Arif
Tasnim
Mahi
Zarif
Araf
Fahad
Ruhan
Sayhan
Labib
Nadim
Shakib
Tanim
Abrar
Ayman
Azhar
Hasan
Farzin
Zain
Rabi
Saad
Tariq
Imran
Zavier
Daiyan
Arvin
Raihan
Mikael
Suhail
Zaki
Faiyaz
Nahiyan
Zuhair
Ahnaf
Mehran
Sarfaraz
Anaya
Myra
Ayat
Zara
Inaya
Aria
Ayla
Zoya
Kiara
Tara
Ira
Diya
Rhea
Siya
Avani
Nyla
"""

# ইউনিক নাম ফিল্টার ও র‍্যান্ডম সাজানো
names_list = list(set([n.strip() for n in raw_names.strip().split("\n") if n.strip()]))
random.shuffle(names_list)

def generate_account_number():
    prefix_pool = ["017", "019", "013", "014"]
    weights = [40, 40, 10, 10]
    prefix = random.choices(prefix_pool, weights=weights, k=1)[0]
    middle = f"{random.randint(10000, 99999)}"
    return f"{prefix}{middle}***"

def send_telegram_photo(caption_text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": IMAGE_URL,
        "caption": caption_text,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, json=payload, timeout=15)
        print(f"Status: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        print(f"Error: {e}")
        return False

# GitHub Actions টাইমআউট থেকে বাঁচতে প্রতি সেশনে সর্বোচ্চ ৩৫টি মেসেজ পাঠাবে (~৪ ঘণ্টা)
# এরপর স্বয়ংক্রিয়ভাবে পরবর্তী নতুন সেশন শুরু হবে
SESSION_LIMIT = 35
sent_count = 0

print(f"সেশন শুরু হয়েছে। মোট নাম সংখ্যা: {len(names_list)}")

while names_list and sent_count < SESSION_LIMIT:
    name = names_list.pop()
    amount = random.randint(20, 100)
    method = random.choice(["Bkash", "Nagad"])
    account = generate_account_number()

    caption = (
        "✨ <b>EARN MAX PAYMENT — WITHDRAWAL SUCCESSFUL</b> 💸\n\n"
        f"👤 <b>User Name:</b> {name}\n"
        f"💰 <b>Amount:</b> ৳ {amount}\n"
        f"💳 <b>Payment Method:</b> {method}\n"
        f"📱 <b>Account Number:</b> {account}\n"
        "⚡ <b>Status:</b> Instant Approved ✅"
    )

    send_telegram_photo(caption)
    sent_count += 1
    print(f"[{sent_count}] পোস্ট সম্পন্ন: {name}")

    if not names_list or sent_count >= SESSION_LIMIT:
        break

    # ৬ থেকে ৮ মিনিট (৩৬০ থেকে ৪৮০ সেকেন্ড) বিরতি
    delay = random.randint(360, 480)
    print(f"অপেক্ষা করা হচ্ছে {delay} সেকেন্ড ({delay//60} মিনিট {delay%60} সেকেন্ড)...")
    time.sleep(delay)

print("বর্তমান সেশন সম্পন্ন। পরবর্তী সেশন ট্রিগার হচ্ছে...")
