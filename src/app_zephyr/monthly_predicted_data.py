import pandas as pd


def get_monthly_pred(city, BASE_DIR):
    data = []
    if city == "Agra":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Agra.csv")
    elif city == "Ahmedabad":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Ahmedabad.csv")
    elif city == "Alwar":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Alwar.csv")
    elif city == "Amaravati":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Amaravati.csv")
    elif city == "Amritsar":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Amritsar.csv")
    elif city == "Asanol":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Asansol.csv")
    elif city == "Bathinda":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Bathinda.csv")
    elif city == "Bengaluru":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Bengaluru.csv")
    elif city == "Chandrapur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Chandrapur.csv")
    elif city == "Delhi":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Delhi.csv")
    elif city == "Dewas":
        data_df = pd.read_csv(
            BASE_DIR+"/src/app_zephyr/monthly_predicted_data/pred_Dewas.csv")
    elif city == "Durgapur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Durgapur.csv")
    elif city == "Faridabad":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Faridabad.csv")
    elif city == "Ghaziabad":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Ghaziabad.csv")
    elif city == "Haldia":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Haldia.csv")
    elif city == "Howrah":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Howrah.csv")
    elif city == "Hyderabad":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Hyderabad.csv")
    elif city == "Jaipur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Jaipur.csv")
    elif city == "Jalandhar":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Jalandhar.csv")
    elif city == "Jodhpur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Jodhpur.csv")
    elif city == "Kanpur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Kanpur.csv")
    elif city == "Kolkata":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Kolkata.csv")
    elif city == "Kota":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Kota.csv")
    elif city == "Lucknow":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Lucknow.csv")
    elif city == "Ludhiana":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Ludhiana.csv")
    elif city == "Nagpur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Nagpur.csv")
    elif city == "Nashik":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Nashik.csv")
    elif city == "Mumbai":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_NaviMumbai.csv")
    elif city == "Noida":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Noida.csv")
    elif city == "Patna":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Patna.csv")
    elif city == "Pune":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Pune.csv")
    elif city == "Satna":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Satna.csv")
    elif city == "Singrauli":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Singrauli.csv")
    elif city == "Tirupati":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Tirupati.csv")
    elif city == "Udaipur":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Udaipur.csv")
    elif city == "Ujjain":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Ujjain.csv")
    elif city == "Varanasi":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Varanasi.csv")
    elif city == "Vijayawada":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Vijayawada.csv")
    elif city == "Visakhapatnam":
        data_df = pd.read_csv(
            BASE_DIR+"/app_zephyr/monthly_predicted_data/pred_Visakhapatnam.csv")
    data = list(data_df["SARIMA"])
    date = list(data_df["date"])
    # print(data)
    # print(date)
    return {"aqi": data, "date": date}
