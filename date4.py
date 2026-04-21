from datetime import datetime, timedelta

now = datetime.now()
new_time = now + timedelta(seconds=5)

print(f"\nThời gian hiện tại: {now.strftime('%H:%M:%S')}")
print(f"Thời gian sau khi thêm 5 giây: {new_time.strftime('%H:%M:%S')}")