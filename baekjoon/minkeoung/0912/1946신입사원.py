import sys

# 입력 최적화를 위해 sys.stdin.read 사용
input = sys.stdin.read

# 입력 전체를 받아서 한 번에 처리
data = input().splitlines()

t = int(data[0])  # 첫 번째 줄에 있는 테스트 케이스 수
index = 1  # 데이터에서 현재 읽을 위치를 나타냄

for _ in range(t):
    n = int(data[index])  # 현재 테스트 케이스에서의 지원자 수
    applicants = []

    # 지원자들의 서류, 면접 성적을 리스트에 저장
    for i in range(1, n + 1):
        paper, interview = map(int, data[index + i].split())
        applicants.append((paper, interview))

    # 서류 성적 기준으로 정렬
    applicants.sort(key=lambda x: x[0])

    # 첫 번째 지원자는 무조건 선발
    count = 1
    best_interview_rank = applicants[0][1]

    # 나머지 지원자들 면접 성적 비교
    for i in range(1, n):
        if applicants[i][1] < best_interview_rank:
            count += 1
            best_interview_rank = applicants[i][1]

    # 결과 출력
    print(count)
    index += n + 1  # 다음 테스트 케이스로 이동
