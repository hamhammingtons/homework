import sqlite3
import requests
import time
from datetime import datetime


def init_db():
    conn = sqlite3.connect(
        "weather_data.db"
    )  # у меня ее нет я просто для примера сделал
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL
        )
    """
    )
    conn.commit()
    return conn


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.61&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["current_weather"]["temperature"]
    return None


def save_to_db(conn, temp):
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO weather (timestamp, temperature) VALUES (?, ?)", (now, temp)
    )
    conn.commit()
    print(f"[{now}] Saved: {temp} celcius")


def main():
    connection = init_db()
    try:
        while True:
            temperature = get_weather()
            if temperature is not None:
                save_to_db(connection, temperature)

            time.sleep(1800)
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
