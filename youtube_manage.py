import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']}")
        print(f"Time: {video['time']}")
        print(f"URL: {video['url']}")
    print("\n")
    print("*"*70)

def add_video(videos):
    title = input("Enter the video title: ")
    time = input("Enter the video time: ")
    url = input("Enter the video URL: ")
    video = ({
        "title": title,
        "time": time,
        "url": url
    })
    
    videos.append(video)
    save_data_helper(videos)
    print("Video added successfully! ")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index to update: "))
    video = videos[index - 1]
    
    video["title"] = input("Enter the new title: ")
    video["time"] = input("Enter the new time: ")
    video["url"] = input("Enter the new URL: ")
    save_data_helper(videos)
    print("Video updated successfully! ")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index to delete: "))
    videos.pop(index - 1)
    save_data_helper(videos)
    print("Video deleted successfully! ")

def main():
    videos = load_data()

    while True:
        print("\n YouTube Manager | choose an option ")
        print("1. List all YouTube videos ")
        print("2. Add a YouTube video ")
        print("3. Update a YouTube video details ")
        print("4. Delete a YouTube video ")
        print("5. Exit the app ")
        
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
                break
            case _:
                print("Invalid choice! Please try again. ")
                
if __name__ == "__main__":
    main()