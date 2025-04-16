from youtube_search import YoutubeSearch

class YoutubeSearcher:
    def search(q: str):
        search_result = YoutubeSearch(q, 1).to_dict()[0]

        text = f"https://youtu.be/{search_result.get('id')}"

        return text

if __name__ == "__main__":
    print(YoutubeSearcher.search("hello"))