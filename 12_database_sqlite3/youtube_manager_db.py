import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
)
''')

def list_all_videos():
    conn.execute("SELECT * FROM  videos")
    rows = cursor.fetchall()
    if not rows:
        print("No videos found in the database.")
    else:
        for row in rows:
            print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?, ?)", (name,time))
    conn.commit()


def update_videos(video_id, new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE  id = ?",(new_name,new_time,video_id))
    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()

def main():
    while True:
        print('\n Youtube Manager | choose an option')
        print('1. List all youtube videos')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete the video')
        print('5. Exit the app')

        choice = input('Enter your choice ')
        #print(videos)

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the name: ")
            time = input("Enter the time: ")
            add_videos(name,time)
        elif choice == '3':
            video_id = input("Enter your video ID: ")
            name = input("Enter the name: ")
            time = input("Enter the time: ")
            update_videos(video_id,name,time)
        elif choice == '4':
            name = input("Enter the name: ")
            time = input("Enter the time: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid Choice')
    
    conn.close()

if __name__ == '__main__':
    main()