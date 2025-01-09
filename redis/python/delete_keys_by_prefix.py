import argparse

import redis

# 명령줄 인자 파싱
parser = argparse.ArgumentParser(description="Redis 키 제거 by prefix")
parser.add_argument("--host", type=str, default="localhost", required=False, help="Redis 호스트 (예: localhost)")
parser.add_argument("--port", type=int, default=6379, required=False, help="Redis 포트 (예: 6379)")
parser.add_argument("--count", type=int, default=100, required=False, help="Scan count")
parser.add_argument("--prefix", type=str, required=True, help="삭제하려는 key의 접두어")
args = parser.parse_args()

# Redis에 연결
r = redis.Redis(host=args.host, port=args.port, db=0)

# 삭제하려는 키의 접두어
prefix = args.prefix
cursor = 0  # SCAN의 초기 커서 값은 0
deleted_count = 0

while True:
    # SCAN 명령으로 키 찾기
    cursor, keys = r.scan(cursor=cursor, match=f"{prefix}*", count=args.count)
    if keys:
        r.delete(*keys)  # 발견된 키 삭제
        deleted_count += len(keys)

    # 커서가 0이면 탐색 종료
    if cursor == 0:
        break

print(f"Deleted {deleted_count} keys with prefix '{prefix}'")
