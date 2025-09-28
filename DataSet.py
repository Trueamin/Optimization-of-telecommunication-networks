import numpy as np
import pandas as pd

# تعداد نمونه‌های دیتاست
num_samples = 1000

# ویژگی‌ها (Features)
np.random.seed(42)
input_power = np.random.uniform(0, 10, num_samples)  # قدرت سیگنال ورودی (dBm)
fiber_length = np.random.uniform(1, 50, num_samples)  # طول کابل (کیلومتر)
temperature = np.random.uniform(-10, 50, num_samples)  # دمای محیط (درجه سانتی‌گراد)
num_connectors = np.random.randint(1, 6, num_samples)  # تعداد اتصالات

# مقدار افت سیگنال (Target)
# افت سیگنال وابسته به توان ورودی، طول کابل و تعداد اتصالات است.
signal_loss = (
    0.2 * fiber_length + 0.1 * num_connectors + 0.05 * (temperature - 20) +
    np.random.normal(0, 0.5, num_samples)  # نویز
)

# ساخت دیتافریم
data = pd.DataFrame({
    "Input Power (dBm)": input_power,
    "Fiber Length (km)": fiber_length,
    "Temperature (°C)": temperature,
    "Number of Connectors": num_connectors,
    "Signal Loss (dB)": signal_loss
})

# ذخیره در فایل CSV
data.to_csv("fiber_optic_dataset.csv", index=False)
print("Dataset created and saved as 'fiber_optic_dataset.csv'")
