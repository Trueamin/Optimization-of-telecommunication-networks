import pandas as pd

# بارگذاری دیتاست
data = pd.read_csv("fiber_optic_dataset.csv")

# نمایش ۵ سطر اول
print(data.head())

# اطلاعات کلی از دیتاست
print("\nاطلاعات دیتاست:")
print(data.info())

# آماره‌های توصیفی
print("\nخلاصه آماری:")
print(data.describe())
