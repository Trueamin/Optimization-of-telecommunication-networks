import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# بارگذاری دیتاست
data = pd.read_csv("fiber_optic_dataset.csv")

# 1. بررسی داده‌های گمشده (Missing Data)
if data.isnull().sum().sum() > 0:
    #print("داده‌های گمشده شناسایی شدند.")
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

#print("پیش‌پردازش کامل شد.")

# 1. ساخت مدل رگرسیون خطی
model = LinearRegression()

# 2. آموزش مدل
model.fit(X_train_scaled, y_train)

# 3. پیش‌بینی روی داده‌های تست
y_pred = model.predict(X_test_scaled)

# 4. ارزیابی مدل
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

#print(f"Mean Squared Error: {mse:.3f}")
#print(f"R^2 Score: {r2:.3f}")

# وزن ویژگی‌ها
feature_importance = model.coef_

# نمایش ویژگی‌های مهم
for feature, importance in zip(X.columns, feature_importance):
    print(f"{feature}: {importance:.3f}")
