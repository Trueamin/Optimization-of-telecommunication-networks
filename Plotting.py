import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# بارگذاری دیتاست
data = pd.read_csv("fiber_optic_dataset.csv")

"""  نمایش ۵ سطر اول
#print(data.head())

# اطلاعات کلی از دیتاست
print("\nاطلاعات دیتاست:")
print(data.info())

# آماره‌های توصیفی
print("\nخلاصه آماری:")
print(data.describe()) """

# توزیع مقدار افت سیگنال
sns.histplot(data["Signal Loss (dB)"], kde=True)
plt.title("Distribution of Signal Loss")
plt.show()

# رابطه بین طول کابل و افت سیگنال
sns.scatterplot(x="Fiber Length (km)", y="Signal Loss (dB)", data=data)
plt.title("Fiber Length vs Signal Loss")
plt.show()

# رابطه بین دما و افت سیگنال
sns.scatterplot(x="Temperature (°C)", y="Signal Loss (dB)", data=data)
plt.title("Temperature vs Signal Loss")
plt.show()
