import pandas as pd


dataframe = pd.read_csv('lottery_results.csv')

THIA_MONTHS = {
    "มกราคม": 1,
    "กุมภาพันธ์": 2,
    "มีนาคม": 3,
    "เมษายน": 4,
    "พฤษภาคม": 5,
    "มิถุนายน": 6,
    "กรกฎาคม": 7,
    "สิงหาคม": 8,
    "กันยายน": 9,
    "ตุลาคม": 10,
    "พฤศจิกายน": 11,
    "ธันวาคม": 12
}
def convert_thai_month_to_english(thai_month):
    """
    Converts Thai month names to English month names.
    """
    return THIA_MONTHS.get(thai_month, thai_month)
def map_thai_day(day):
        thai_days = {
            "Monday": "จันทร์",
            "Tuesday": "อังคาร",
            "Wednesday": "พุธ",
            "Thursday": "พฤหัสบดี",
            "Friday": "ศุกร์",
            "Saturday": "เสาร์",
            "Sunday": "อาทิตย์"
        }
        return thai_days.get(day, day)

def add_date_detail(df):
    """
    Adds additional date details to the DataFrame.
    """
    # Convert the 'Date' column to datetime format
    # Create Date time "2023-10-01"
    df['Month'] = df['Month'].apply(convert_thai_month_to_english)
    df['Datetime'] = pd.to_datetime(
        (df['Years'] - 543).astype(str) + '-' +
        df['Month'].apply(lambda x: list(THIA_MONTHS.values()).index(x) + 1).astype(str).str.zfill(2) + '-' +
        df['Date'].astype(str).str.zfill(2),
        format='%Y-%m-%d'
    )

    # Extract day of the week (0=Monday, 6=Sunday)
    df['day_of_week'] = df['Datetime'].dt.dayofweek

    # Extract full month name

    # Extract full weekday name
    df['weekday_name'] = df['Datetime'].dt.day_name()

    
    
    df['weekday_name'] = df['weekday_name'].apply(map_thai_day)
    
    return df


new_dataframe = add_date_detail(dataframe)

dataframe

new_dataframe.to_csv('lottery_results_with_thai_date_details.csv', index=False)
print("Date details added successfully.")