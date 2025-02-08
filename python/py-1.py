import mysql.connector
 
def create_database():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="news_feed"
    )
    cursor = conn.cursor()

def add_news():
    title = input("Enter News Title: ")
    description = input("Enter News Details: ")
    image_path = input("Enter Photo Path or URL: ")
    
    conn =mysql.connector.connect( host="localhost",
        user="root",
        password="",
        database="news_feed")
    c=conn.cursor()
    c.execute(  "INSERT INTO news (title, description, image_path) VALUES (%s, %s, %s)",
        (title, description, image_path))
    
    conn.commit()
    conn.close()
    print("News added successfully!")
    
def list_news():
    page = 1
    while True:
        conn = mysql.connector.connect(
            host="localhost", user="root", password="", database="news_feed"
        )
        c = conn.cursor()
        
        per_page = 5
        offset = (page - 1) * per_page

        c.execute("SELECT * FROM news LIMIT %s OFFSET %s", (per_page, offset))
        news_items = c.fetchall()

        if not news_items:
            print("No more news to display.")
            break

        print(f"Displaying page {page}")
        for news in news_items:
            print(f"ID: {news[0]}")
            print(f"Title: {news[1]}")
            print(f"Description: {news[2]}")
            print(f"Image Path: {news[3]}")
            print("-" * 40)

        conn.close()

        next_page = input("Would you like to see the next page? (y/n): ").lower()
        if next_page == 'y':
            page += 1
        else:
            break

    
def main_menu():
    while True:
            print("\nSelect your choice")
            print("1. Add news details")
            print("2. List news")
            print("3. Exit app")
            choice = input("Enter your choice: ")

            if choice == "1":
                add_news()
            elif choice == "2":
                list_news()
            elif choice == "3":
                print("Exiting app...")
                break
            else:
                print("Invalid choice. Please try again.")
                
if __name__ == "__main__":
    create_database()  
    main_menu()



