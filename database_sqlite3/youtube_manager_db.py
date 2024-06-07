import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    time TEXT NOT NULL,
    url TEXT NOT NULL
)           
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()

    print("\n")
    print("*"*70)
    for video in videos:
        print(f"{video[0]}. {video[1]}")
        print(f"Time: {video[2]}")
        print(f"URL: {video[3]}")
    print("\n")
    print("*"*70)
    
def add_video():
    title = input("Enter video title: ")
    time = input("Enter video time: ")
    url = input("Enter video URL: ")

    cursor.execute("INSERT INTO videos (title, time, url) VALUES (?, ?, ?)", (title, time, url))
    conn.commit()

    print("Video added successfully!")

def update_video():
    list_videos()
    video_id = int(input("Enter video ID to update: "))

    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()

    if video:
        title = input("Enter new video title: ")
        time = input("Enter new video time: ")
        url = input("Enter new video URL: ")

        cursor.execute("UPDATE videos SET title = ?, time = ?, url = ? WHERE id = ?", (title, time, url, video_id))
        conn.commit()

        print("Video updated successfully!")
    else:
        print("Invalid video ID.")

def delete_video():
    list_videos()
    video_id = int(input("Enter video ID to delete: "))

    cursor.execute("SELECT * FROM videos WHERE id = ?", (video_id,))
    video = cursor.fetchone()

    if video:
        cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
        conn.commit()

        print("Video deleted successfully!")
    else:
        print("Invalid video ID.")
        

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            add_video()
        elif choice == "3":
            update_video()
        elif choice == "4":
            delete_video()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
            
    conn.close()


if __name__ == '__main__':
    main()