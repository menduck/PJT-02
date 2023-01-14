import requests
from pprint import pprint

import os
from dotenv import load_dotenv
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

import f04
def credits(title):
    try :
        movie_id = f04.search_movie(title)
        credits_url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}&language=ko-KR'

        res = requests.get(credits_url).json()
        casts = res.get('cast')
        crews = res.get('crew')

        casts = [cast['name'] for cast in casts if cast.get("cast_id") < 10]
        directing = [crew['name'] for crew in crews if crew.get("department") == "Directing"]
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
