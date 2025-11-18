from pyrogram import Client
import os

api_id = int(os.getenv("API_ID", 123456))
api_hash = os.getenv("API_HASH", "your_api_hash")

with open("accounts.txt") as f:
    nums = [x.strip() for x in f]

for num in nums:
    print("Login for:", num)
    app = Client(f"sessions/{num}", api_id, api_hash)
    app.start()
    print("Logged in:", num)
    app.stop()
