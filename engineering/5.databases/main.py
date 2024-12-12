import psycopg2

db_connection_params = {"dbname": "postgres",
                        "user": "postgres",
                        "host": "localhost",
                        "port": "5432",
                        "password": "Gazprom09",}

def get_tasks_from_db(db_creds: dict):
    with psycopg2.connect(**db_creds) as connection:
        with connection.cursor() as cursor:
            cursor.execute(R"""
                SELECT c.name, c.desc, c.due, array_agg(l.name)
                FROM python_test.cards c
                JOIN python_test.tasks_labels tl ON c.id = tl.task_id
                JOIN python.test.labels l ON l.id = tl.label_id
                GROUP BY c.name, c_desc, c.due
            """)
            records = cursor.fetchall()
            print(records)
            connection.commit()
            cursor.execute("INSERT INTO python_test.cards (name, \"desc\", due, labels) VALUES (%s, %s, %s)", ["test_task", "test_task_desc", "2023-03-05"])


def main():
    return


if __name__ == '__main__':
    main()