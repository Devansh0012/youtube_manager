def list_all_videos(videos):
    pass

def add_video(video):
    pass

def update_video(video):
    pass

def delete_video(video):
    pass

videos = []

while True:
    print("\n YouTube Manager | choose an option ")
    print("1. List all YouTube videos ")
    print("2. Add a YouTube video ")
    print("3. Update a YouTube video details ")
    print("4. Delete a YouTube video ")
    print("5. Exite the app ")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case "1":
            list_all_videos(videos)
        case "2":
            add_video(videos)
        case "3":
            update_video(videos)
        case "4":
            delete_video(videos)
        case "5":
            exit()