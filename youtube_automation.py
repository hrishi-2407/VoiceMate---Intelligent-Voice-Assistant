import requests
import urllib.parse
import webbrowser

def poyt(topic):
    # Encode the search query
    search_query = urllib.parse.quote(topic)
    
    # Perform a search request
    url = f"https://www.youtube.com/results?search_query={search_query}"
    response = requests.get(url)
    
    # Find the first video result
    search_results = response.text
    start_index = search_results.find('/watch?v=')
    
    if start_index != -1:
        # Extract the video ID
        video_id = search_results[start_index+9:start_index+20]
        
        # Construct the full video URL
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        
        # Open the video in the default web browser
        webbrowser.open(video_url)
        
        print(f"Playing YouTube video: {topic}")
    else:
        print(f"No YouTube video found for: {topic}")

# # Example usage
# if __name__ == "__main__":
#     poyt("play the song saajna and aadat mashup by jalraj")