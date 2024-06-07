import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.p6qft2w.mongodb.net/")

db = client["ytmanager"]
collection = db["videos"]

print(collection)

def list_videos():
    videos = collection.find()
    for video in videos:
        print(video)

def add_video():
    title = input("Enter video title: ")
    description = input("Enter video description: ")
    url = input("Enter video URL: ")

    video = {
        "title": title,
        "description": description,
        "url": url
    }

    collection.insert_one(video)
    print("Video added successfully")

def update_video():
    video_id = input("Enter video ID to update: ")
    title = input("Enter new video title: ")
    description = input("Enter new video description: ")
    url = input("Enter new video URL: ")

    video = {
        "title": title,
        "description": description,
        "url": url
    }
    collection.update_one({"_id": video_id}, {"$set": video})
    print("Video updated successfully")

def delete_video():
    video_id = input("Enter video ID to delete: ")
    collection.delete_one({"_id": video_id})
    print("Video deleted successfully")

def main():
    while True:
        print("\n YouTube Manage App")
        print("1. List all videos ")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()