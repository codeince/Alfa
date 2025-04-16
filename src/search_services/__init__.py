from youtube_search import YoutubeSearch
from duckduckgo_search import DDGS

class BaseSearcher:
    def __init__(self, base_url: str = "https://www.example.com/"):
        self.base_url = base_url

    def search(q: str) -> str:
        return q

class YoutubeSearcher(BaseSearcher):
    def __init__(self):
        super("https://youtube.com/")

    def search(q: str) -> str:
        search_result = YoutubeSearch(q, 1).to_dict()[0]

        text = f"https://youtu.be/{search_result.get('id')}"

        return text
    
class DuckDuckGoSearcher(BaseSearcher):
    def __init__(self):
        super().__init__("https://duckduckgo.com/")

    def search(q: str) -> str:
        search_result = DDGS().text(q, max_results=1)[0]
        
        text = search_result.get('body')

        return text

SEARCHERS: list[BaseSearcher] = [YoutubeSearcher, DuckDuckGoSearcher]

class RootSearcher:
    def __init__(self):
        self.searcher = self._find_best_searcher()

    def _find_best_searcher(self):
        for searcher in SEARCHERS:
            try:
                text = searcher.search("hello")
                return searcher
            except:
                continue

    def search(self, q: str):
        return self.searcher.search(q)


if __name__ == "__main__":
    print(RootSearcher().search("hello"))