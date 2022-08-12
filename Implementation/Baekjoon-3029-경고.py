## 구현(Implementation)
## Baekjoon 3029 경고
## https://www.acmicpc.net/problem/3029

now_hour, now_minute, now_seconds = map(int, input().split(":"))
throw_hour, throw_minute, throw_seconds = map(int, input().split(":"))

temp_now_total_seconds = now_hour * 60 * 60 + now_minute * 60 + now_seconds
temp_throw_total_seconds = throw_hour * 60 * 60 + throw_minute * 60 + throw_seconds

temp_sub_seconds = 0

if temp_throw_total_seconds > temp_now_total_seconds:
    temp_sub_seconds = temp_throw_total_seconds - temp_now_total_seconds
else:
    temp_sub_seconds = temp_throw_total_seconds - temp_now_total_seconds + 24*60*60

sub_hour = temp_sub_seconds//(60*60)
temp_sub_seconds %= 60*60
sub_minute = temp_sub_seconds//60
temp_sub_seconds %= 60
sub_seconds = temp_sub_seconds%60

print("%02d:%02d:%02d" % (sub_hour, sub_minute, sub_seconds))