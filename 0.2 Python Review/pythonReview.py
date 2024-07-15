def create_youtube_vid(title, description):
    
    new_youtube_vid = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return new_youtube_vid

def like(youtube_vid):
    
    if 'likes' in youtube_vid:
        youtube_vid['likes'] += 1
    return youtube_vid

def dislike(youtube_vid):
    
    if 'dislikes' in youtube_vid:
        youtube_vid['dislikes'] += 1
    return youtube_vid

def add_comment(youtube_vid, username, comment_text):
    
    if 'comments' not in youtube_vid:
        youtube_vid['comments'] = {}
    
    if username not in youtube_vid['comments']:
        youtube_vid['comments'][username] = []
    
    youtube_vid['comments'][username].append(comment_text)
    return youtube_vid

# try things
youtube_video = create_youtube_vid("My Funny Video", "Funny video description.")

# like function
youtube_video = like(youtube_video)
print("After like:", youtube_video)  # likes should be 1

# dislike function
youtube_video = dislike(youtube_video)
print("After dislike:", youtube_video)  # dislikes should be 1

# add_comment function
youtube_video = add_comment(youtube_video, "user1", "Great video!")
print("After adding comment:", youtube_video)  # should have one comment from 'user1'

# likes (495 times)
for _ in range(999):
    youtube_video = like(youtube_video)

print("After adding 999 likes:", youtube_video)  # likes should be 496 (1 + 495)
