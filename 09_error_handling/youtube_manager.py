# we need to take inputs from the user as a choice
import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test =  json.load(file) #load that data into json and read the data
            #print(type(test)) #this is a list but a json list
            return test
    except FileNotFoundError:
        return []
  
def save_data_helper(videos):
      with open('youtube.txt','w') as file:
           return json.dump(videos,file)

def list_all_videos(videos): #we need to provide indexing here
    print('\n')
    print('*' * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration : {video['time']}")
    print('\n')
    print('*' * 70)

def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name':name , 'time':time})
    save_data_helper(videos)
    
    
def update_videos(videos):
    list_all_videos(videos)
    index = int(input("Enter the list number you want to delete: "))
    if   1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid Index selected")

def delete_videos(videos):
    list_all_videos(videos)
    index = int(input('Enter the index you want to delete'))
    if   1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")



def main():
    videos = load_data()
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
            list_all_videos(videos)
        elif choice == '2':
            add_videos(videos)
        elif choice == '3':
            update_videos(videos)
        elif choice == '4':
            delete_videos(videos)
        elif choice == '5':
            break
        else:
            print('Invalid Choice')
            
if __name__ == '__main__':
    main()