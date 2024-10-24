from file1 import client

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    pass


def add_videos(name,time):
    pass

def update_videos(video_id,name,time):
    pass

def delete_videos(video_id):
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
            video_id = input("Enter your video id to update: ")
            name = input("Enter the updated name: ")
            time = input("Enter the updated time: ")
            update_videos(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter your video id to update: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid Choice')

if __name__ == '__main__':
    main()



