# we need to take inputs from the user as a choice
import json

def load_data():
    pass
    try:
        with open('youtube.txt','r') as file:
            return json.loads(file) #load that data into json and read the data
    except FileNotFoundError:
        return []
  
def save_data_helper(videos):
      with open('youtube.txt','w') as file:
           return json.dump(videos,file)

def list_all_videos(videos):
    pass

def add_videos(videos):
    pass

def update_videos(videos):
    pass

def delete_videos(videos):
    pass



def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | choose an option')
        print('1. List all youtube videos')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete the video')
        print('5. Exist the app')
        
        choice = input('Enter your choice ')
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print('Invalid Choice')
            
if __name__ == '__main__':
    main()