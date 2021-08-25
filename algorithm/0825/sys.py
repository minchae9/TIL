import sys
sys.stdin = open('input.txt', 'r')
# stdin: 외부입력과 콘솔 연결 통로
# 버퍼 최대 용량 넘어가면 뒤에 들어오는 애가 앞을 덮어씀.
# 입력이 1MB 초과하면, 여기서 input 바로 넣으면 안 되고 sys.stdin 써야 함
# 콘솔로 연결된 stdin을 파일로 연결시키는 역할!

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{} {}'.format(tc, N))