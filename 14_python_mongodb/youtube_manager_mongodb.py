from file1 import client
from bson import ObjectId

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"Id:{video['_id']},Name:{video['name']},Time: {video['time']}")


def add_videos(name,time):
    video_collection.insert_one({"name":name,"time":time})

def update_videos(video_id,new_name,new_time):
    video_collection.update_one(
        {'_id':ObjectId(video_id)},
        {"$set": {"name":new_name, "time":new_time}}
    )

def delete_videos(video_id):
    video_collection.delete_one({"_id":ObjectId(video_id)})


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



