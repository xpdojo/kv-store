import argparse
import time
from collections import defaultdict
from pprint import pprint

import redis

# 명령줄 인자 파싱
parser = argparse.ArgumentParser(description="Redis 키 그룹 집계")
parser.add_argument("--host", type=str, default="localhost", required=False, help="Redis 호스트 (예: localhost)")
parser.add_argument("--port", type=int, default=6379, required=False, help="Redis 포트 (예: 6379)")
parser.add_argument("--count", type=int, default=100, required=False, help="Scan count")
args = parser.parse_args()

# Redis에 연결
r = redis.Redis(host=args.host, port=args.port, db=0)

# SCAN으로 키 탐색 및 그룹화
cursor = 0
group_counts = defaultdict(int)  # 그룹별 개수를 저장할 딕셔너리

while True:
    # SCAN으로 키 가져오기
    cursor, keys = r.scan(cursor=cursor, match="*", count=args.count)
    for key in keys:
        key_str = key.decode("utf-8")  # Redis 키는 바이트 문자열이므로 디코딩
        group = "no_prefix"
        split = key_str.split(':')
        # if split contains prefix "U20" then group is "U20"
        if split[0].startswith("U20"):
            group = "U20"
        elif len(split) == 1:
            group = split[0]
        elif len(split) > 1:
            group = f"{split[0]}:{split[1]}"
        group_counts[group] += 1

    # 커서가 0이면 탐색 종료
    if cursor == 0:
        break
    print("sleep 0.5")
    pprint(group_counts)
    time.sleep(0.5)  # 너무 빠른 탐색을 방지하기 위해 0.5초 대기

# 결과 출력
for group, count in group_counts.items():
    pprint(f"Group '{group}' has {count} keys")
