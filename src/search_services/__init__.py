from youtube_search import YoutubeSearch
from ddg import Duckduckgo

from random import choice

class BaseSearcher:
    def __init__(self, base_url: str = "https://www.example.com/"):
        self.base_url = base_url

    def search(q: str) -> str:
        return q

class YoutubeSearcher(BaseSearcher):
    def __init__(self):
        super("https://youtube.com/")

    def search(q: str) -> str:
        search_result = choice(YoutubeSearch(q, 20).to_dict())

        text = f"https://youtu.be/{search_result.get('id')}"

        return text
    
class DuckDuckGoSearcher(BaseSearcher):
    def __init__(self):
        super().__init__("https://duckduckgo.com/")

    def search(q: str) -> str:
        search_result = Duckduckgo().search(q)
        
        if search_result.get('success'):
            text = choice(search_result.get('data')).get('description')
        else:
            raise ConnectionError('Errored')

        return text

SEARCHERS: list[BaseSearcher] = [DuckDuckGoSearcher, YoutubeSearcher]

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
        try:
            return self.searcher.search(q)
        except:
            self.searcher = self._find_best_searcher()
            try:
                return self.searcher.search(q)
            except:
                return "{connection_error}"


if __name__ == "__main__":
    print(RootSearcher().search("hello"))