import argparse
import time

import redis

# 명령줄 인자 파싱
parser = argparse.ArgumentParser(description="Redis 키 찾기 by prefix")
parser.add_argument("--host", type=str, default="localhost", required=False, help="Redis 호스트 (예: localhost)")
parser.add_argument("--port", type=int, default=6379, required=False, help="Redis 포트 (예: 6379)")
parser.add_argument("--count", type=int, default=100, required=False, help="Scan count")
parser.add_argument("--prefix", type=str, required=True, help="찾으려는 key의 접두어")
args = parser.parse_args()

# Redis에 연결
r = redis.Redis(host=args.host, port=args.port, db=0)

# SCAN을 사용하여 특정 패턴의 키 찾기
prefix = args.prefix
cursor = 0  # SCAN의 초기 커서 값은 0
keys_found = []

while True:
    # SCAN 명령 실행
    cursor, keys = r.scan(cursor=cursor, match=f"{prefix}*", count=args.count)
    keys_found.extend(keys)  # 발견된 키 저장
    if keys_found:
        print(keys_found)

    # 커서가 0이면 탐색 종료
    if cursor == 0:
        break
    time.sleep(0.5)  # 너무 빠른 탐색을 방지하기 위해 0.5초 대기

print(f"Found {len(keys_found)} keys with prefix '{prefix}'")
for key in keys_found:
    print(key.decode("utf-8"))  # 바이트 문자열을 문자열로 변환하여 출력
