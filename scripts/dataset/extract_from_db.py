import csv
import pymysql

from ampdb_config import db_config


OUTPUT_FILE = "confirmed_amp_urls.csv"
LIMIT = 1000

"""

amp. .amp amp_articleshow /amp/

"""

def main():
    connection = pymysql.connect(**db_config)

    try:
        with connection.cursor() as cursor:
#            cursor.execute(
#                """
#                SELECT id, amp
#                FROM fetched_urls
#                ORDER BY id ASC
#                LIMIT %s
#                """,
#                (LIMIT,),
#            )

#            cursor.execute(
#                """
#                SELECT id, amp
#                FROM fetched_urls
#                WHERE id >= %s
#                ORDER BY id ASC
#                LIMIT %s
#                """,
#                (50001, 1000),
#            )

#            cursor.execute(
#                """
#                SELECT id, amp
#                FROM fetched_urls
#                WHERE id > %s
#                ORDER BY RAND()
#                LIMIT %s
#                """,
#                (50001, 1000),
#            )

            cursor.execute(
                """
                SELECT id, amp
                FROM fetched_urls
                WHERE amp IS NOT NULL
                AND amp != ''
                AND amp NOT LIKE '%%amp.%%'
                AND amp NOT LIKE '%%.amp%%'
                AND amp NOT LIKE '%%amp_articleshow%%'
                AND amp NOT LIKE '%%/amp/%%'
                ORDER BY RAND()
                LIMIT %s
                """,
                (49,),
            )

            rows = cursor.fetchall()

        with open(OUTPUT_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "url"])
            writer.writerows(rows)

        print(f"Saved {len(rows)} AMP URLs to {OUTPUT_FILE}")

    finally:
        connection.close()


if __name__ == "__main__":
    main()
