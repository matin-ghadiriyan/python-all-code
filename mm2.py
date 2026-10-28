# import requests
# TOKEN = '1874306625:Zd3Y5csXtnpPZNkDPcXhhnPrc219j7959e4'
# r = requests.get(url=f'https://tapi.bale.ai/bot{TOKEN}/getUpdates?limit=1')
# print(r.json())

import requests

# لطفاً توکن ربات خود را در اینجا قرار دهید
TOKEN = '1874306625:Zd3Y5csXtnpPZNkDPcXhhnPrc219j7959e4' 
url = f'https://tapi.bale.ai/bot{TOKEN}/getWebhookInfo'
# Mohamadmatinmatin2@gmail.com
# Mohama@d4m454atinmati
try:
    r = requests.get(url)
    r.raise_for_status() # اگر درخواست ناموفق بود، خطایی ایجاد می‌کند
    webhook_info = r.json()
    print(webhook_info)

    # تفسیر نتایج بر اساس مستندات شما:
    if 'result' in webhook_info and 'url' in webhook_info['result']:
        webhook_url = webhook_info['result']['url']
        if webhook_url:
            print(f"\nوضعیت وب‌هوک: تنظیم شده است.")
            print(f"آدرس وب‌هوک: {webhook_url}")
        else:
            print(f"\nوضعیت وب‌هوک: تنظیم نشده است (ربات در حال استفاده از متد getUpdates است).")
    else:
        print("\nخطا در دریافت اطلاعات وب‌هوک یا فرمت پاسخ نامعتبر است.")

except requests.exceptions.RequestException as e:
    print(f"خطایی در ارسال درخواست رخ داد: {e}")
except ValueError:
    print("خطایی در پردازش پاسخ JSON رخ داد.")