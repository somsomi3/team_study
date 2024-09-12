N,M = map(int,input().split()) # N열 M행
arr = [list(input()) for _ in range(N)]
cnt_lst = []
for a in range(N-8+1):
    for b in range(M-8+1):
        w_cnt = 0  # 홀:검 짝:흰
        b_cnt = 0  # 홀:흰 짝:검
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 == 0:
                    # b_cnt 짝수 부분 : 검
                    if arr[i][j] == 'W':
                        b_cnt += 1
                    # w_cnt 짝수 부분 : 흰
                    else:
                        w_cnt += 1
                else:
                    # b_cnt 홀수 부분 : 흰
                    if arr[i][j] == 'B':
                        b_cnt += 1
                    # w_cnt 홀수 부분 : 검
                    else:
                        w_cnt += 1

        cnt_lst.append(min(w_cnt, b_cnt))

result = min(cnt_lst)
print(result)