def solution(genres, plays):
    answer = []
    
    genre_dic = {}          #key = genre, values = [count_play, index]
    genre_total_play = {}   #key = genre, values = total_count_play
    
    for i in range(len(genres)): 
        #add genre and start to count play
        
        if genres[i] not in genre_dic.keys(): 
            genre_dic[genres[i]] = [(plays[i], i)] 
            genre_total_play[genres[i]] = plays[i] 
        else: 
            genre_dic[genres[i]].append((plays[i], i)) 
            genre_total_play[genres[i]] += plays[i]
    
    #sorting counts_total_play
    genre_total_play = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    
    #find 2 plays
    for key in genre_total_play: 
        play_list = genre_dic[key[0]] 
        play_list = sorted(play_list, key = lambda x : (-x[0], x[1])) 
        
        for i in range(len(play_list)): 
            if i == 2: 
                break 
            answer.append(play_list[i][1])
            
    return answer