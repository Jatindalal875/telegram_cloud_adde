from pyrogram import Client
import os

api_id = int(os.getenv("API_ID", 27417670))
api_hash = os.getenv("API_HASH", "26bc34db2712e4b099d1918bd59271bf")

with open("accounts.txt") as f:
    nums = [x.strip() for x in f]

for num in nums:
    print("Login for:", num)
    app = Client(f"sessions/{num}", api_id, api_hash)
    app.start()
    print("Logged in:", num)
    app.stop()
