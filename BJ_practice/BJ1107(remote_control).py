N = input("몇 번 채널로 갈지 입력:")
M = int(input("버튼이 몇개나 고장이 났는지 입력 "))
c_list = (input("고장이 난 버튼 입력")).split() # 아직 문자열
N_list = []
button = [1,2,3,4,5,6,7,8,9]
c_list = [int(i) for i in c_list] #문자열 리스트 정수로 변환
res = []

for i in range(0,M):  #숫자로 입력가능한 숫자 선별
    button.remove(c_list[i])

for i in N:
    N_list.append(int(i))

for i in range(0,len(N_list)):
    if N_list in button:
        res.append(i)  # append가 뒤에 오는거 생각하고 다시 고치기
    else:
        


#N_list와 선별된 button 리스트를 비교하며 버튼 리스트에 N_list 값이 없을 경우 그와 가까운 
# 숫자로 변경 (플러스로 계산할지 마이너스로 계산할지 정해야함)