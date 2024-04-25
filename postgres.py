import psycopg2
from dotenv import load_dotenv
import os


months = {
    'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
    'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12
}


def check_purchase_length(subject, first_name, last_name, classyear, type, potok, month):
    load_dotenv()

    db_params = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }
    if classyear == "ОГЭ":
        classyear = "9 класс"
    elif classyear == "ЕГЭ":
        classyear = '11 класс'

    month_number = months.get(month.lower(), None)
    if month_number is None:
        return None

    sql_query = f"""
       
    """

    conn = psycopg2.connect(**db_params)
    try:
        with conn.cursor() as cur:
            cur.execute(sql_query)
            result = cur.fetchone()

            if result:
                return result[0] # Возвращаем значение первого столбца (mp.id)
            else:
                return None
    finally:
        conn.close()
