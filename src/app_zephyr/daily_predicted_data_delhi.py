import pandas as pd


def get_daily_delhi_pred(BASE_DIR):
    data_df = pd.read_csv(
        BASE_DIR + "/app_zephyr/daily_predicted_data_delhi/predicted_delhi.csv")
    data = list(data_df["AQI"])
    date = list(data_df["Date"])
    # print(data)
    # print(date)
    return {"aqi": data, "date": date}
