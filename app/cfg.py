from decouple import config

BRAND_ACCOUNT_NUMBER = config("BRAND_ACCOUNT_NUMBER")

DB_CONNSTR = config("DB_CONNSTR")

COOKIE = config('COOKIE')

HEADERS_AUTH_DICT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "X-Goog-AuthUser": "0",
    "x-origin": "https://music.youtube.com",
    "Cookie": COOKIE,
}