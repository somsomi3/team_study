#1018체스판 다시 칠하기

import sys

def sliding_window(board):
    n = len(board)  # 체스판의 행 수
    m = len(board[0])  # 체스판의 열 수
    min_changes = float('inf')  # 다시 칠해야 하는 최소 칸 수

    # 슬라이딩 윈도우로 8x8 체스판 확인
    for i in range(n - 7):  # 시작 행 위치
        for j in range(m - 7):  # 시작 열 위치
            w_changes = 0  # 왼쪽 위가 흰색으로 시작하는 경우
            b_changes = 0  # 왼쪽 위가 검정색으로 시작하는 경우

            # 8x8 크기의 체스판 내부를 확인
            for x in range(8):
                for y in range(8):
                    current = board[i + x][j + y]  # 현재 칸의 색

                    # (x + y) 합에 따라 정상 체스판의 색을 결정
                    if (x + y) % 2 == 0:  # 짝수인 경우
                        if current != 'W':  # 흰색이어야 하는데 다른 경우
                            w_changes += 1
                        if current != 'B':  # 검정색이어야 하는데 다른 경우
                            b_changes += 1
                    else:  # 홀수인 경우
                        if current != 'B':  # 검정색이어야 하는데 다른 경우
                            w_changes += 1
                        if current != 'W':  # 흰색이어야 하는데 다른 경우
                            b_changes += 1

            # 최소 변경 횟수 갱신
            min_changes = min(min_changes, w_changes, b_changes)

    return min_changes


def main():
    input = sys.stdin.read
    data = input().splitlines()

    # 체스판의 크기 (첫 번째 입력 줄)
    n, m = map(int, data[0].split())

    # 체스판을 2차원 리스트로 변환
    board = [list(line) for line in data[1:n + 1]]

    # 슬라이딩 윈도우 방식으로 최소 변경 횟수 계산
    result = sliding_window(board)

    print(result)


if __name__ == "__main__":
    main()
