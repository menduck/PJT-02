import requests
from pprint import pprint

import os
from dotenv import load_dotenv
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

def search_movie(title):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=ko-KR&query={title}&region=KR'

    res = requests.get(url).json()
    data = res['results']
    target_movie_id = data[0]['id']

    try:
        return target_movie_id
    except:
        return None

def credits(title):
    movie_id = search_movie(title)
    credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR'

    res = requests.get(credits_url).json()
    casts = res.get('cast')
    crews = res.get('crew')

    casts = [i['name'] for i in casts if i.get("cast_id") < 10]
    directing = [i['name'] for i in crews if i.get("department") == "Directing"]
    try :
        return {'cast': casts, 'directing': directing}
    except:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
