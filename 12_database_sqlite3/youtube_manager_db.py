import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor

cursor.execute('''
               CREATE TABLE IF NOT EXIST videos(
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
)
''')

def list_all_videos():
    pass

def add_videos():
    pass 


def update_videos():
    pass

def delete_videos():
    pass

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


if __name__ == '__main__':
    main()