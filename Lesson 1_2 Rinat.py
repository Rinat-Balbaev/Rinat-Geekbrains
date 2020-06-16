user_time_sec = int(input('Input time in sec: '))

time_hours = user_time_sec // 3600
time_mins = (user_time_sec - time_hours * 3600) // 60
time_secs = user_time_sec - (time_hours * 3600 + time_mins * 60)

print(f"Result is {time_hours}h:{time_mins}m:{time_secs}s")

