access_logs = (101, 105, 101, 102, 101, 108, 105)

user_101_count = access_logs.count(101)

# User ID 102 ka first index  
user_102_index = access_logs.index(102)

# Results print karein
print("User ID 101 accessed database:", user_101_count, "times")
print("User ID 102 first logged at index:", user_102_index)