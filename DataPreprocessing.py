import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# بارگذاری دیتاست
data = pd.read_csv("fiber_optic_dataset.csv")

# 1. بررسی داده‌های گمشده (Missing Data)
if data.isnull().sum().sum() > 0:
    print("داده‌های گمشده شناسایی شدند.")
    data = data.dropna()  # حذف داده‌های ناقص

# 2. جدا کردن ویژگی‌ها و خروجی
X = data[["Input Power (dBm)", "Fiber Length (km)", "Temperature (°C)", "Number of Connectors"]]
y = data["Signal Loss (dB)"]

# 3. تقسیم داده‌ها به مجموعه آموزش و تست
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. نرمال‌سازی داده‌ها
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("پیش‌پردازش کامل شد.")
