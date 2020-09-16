def solution(genres, plays):
    answer = []
    #key = genre, values = [count_play, index]
    genre_dic = {genre:[] for genre in set(genres)}

    for e in zip(genres, plays, range(len(plays))):
        genre_dic[e[0]].append([e[1] , e[2]])

    #sort by count_play
    genreSort =sorted(list(genre_dic.keys()), key= lambda x: sum([genre[0] for genre in genre_dic[x]]), reverse = True)
    
    #find 2 indexes sorted by count_play
    for genre in genreSort:
        temp = [e[1] for e in sorted(genre_dic[genre],key= lambda x:x[0], reverse = True)]
        answer += temp[:2]

    return answer