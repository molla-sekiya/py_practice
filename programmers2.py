# record를 for문으로 돌리면서 reco_split = reco.split()
# reco_split의 각 요소들을 각 변수들에 집어넣는다
# ex) reco_split[0]은 명령어(enter 등) reco_split[1]은 딕셔너리 변수 user_id에 키값으로 주고
# reco_split[2]는 닉네임으로 user_id의 밸류로 준다 
# for문을 돌리면서 reco_split[0]이 change 일 경우에는
# user_id 키 값에서 reco_split[1]과 같을 경우에는 reco_split[2]인 닉네임을 user_id의
# 그 키값에 대입한다 
# 그 후 anwser리스트에

def solution(record):
    answer = []
    user_id = {}
    command = []
    for reco in record:
        reco_split = reco.split()
        if reco_split[0] == 'Change':  #chage일 경우 user_id의 닉네임을 바꿈
            for id in user_id:
                if id == reco_split[1]:
                    user_id[id] = reco_split[2]       
        else:  #아니면은 커맨드에 그냥 추가함
            command.append([ reco_split[0], reco_split[1]])
        if reco_split[1] not in user_id:   #유저 아디가 user_id 변수에 없을 경우 추가 
            user_id[reco_split[1]] = reco_split[2]
            
    for com in command:
        if com[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(user_id[com[1]]))
        elif com[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(user_id[com[1]]))

    return answer
