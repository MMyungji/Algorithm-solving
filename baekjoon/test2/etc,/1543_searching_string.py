'''
백준 1543번 문서 검색

정규식 사용 - 검색 단어를 1로 변환해서(replace사용) > 이중 for문 사용 지양

'''

string = input()
word = input()
n_string = len(string)
n_word = len(word)

count = 0
visited = [False]*len(string)

for i in range(n_string):
    w = string[i:i+n_word]
    if w == word and visited[i] == False:
        count+=1
        for j in range(i,i+n_word):
            visited[j] = True
print(count)


