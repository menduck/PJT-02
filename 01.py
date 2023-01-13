import requests

import os
from dotenv import load_dotenv
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def popular_count():
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}'

    res = requests.get(url).json()
    popular_data = res['results']
    return len(popular_data)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
