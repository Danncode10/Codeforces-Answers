# Link: https://codeforces.com/contest/2068/problem/C

# Notes:
# Ad triggers if 25 minutes pass (k) since the last ad OR 3 videos are watched
# k wont trigger unless first ad appears


# FAILED TO ANSWER

'''

# MY ANSWER

n = int(input())

answers = []
for i in range(n):
    m,k = list(map(int, input().split()))
    vid_length = list(map(int, input().split()))

    ad_played = 0
    min_played = 0
    vid_count = 0
    first_ad_played = False

    for j in range(m):

        min_played += vid_length[j]
        vid_count += 1

        if vid_count == 3: # if 3 videos played. Note i starts at 0 ... (i+1) add parenthesis take note
            ad_played += 1
            vid_count = 0
            min_played = 0 # reset the min played back to zero, whenever it starts again
            first_ad_played = True

        if first_ad_played and min_played >= k:
                ad_played += 1
                min_played = 0
                vid_count = 0


    answers.append(ad_played)

for ans in answers:
    print(ans)

'''

# A.I. ANSWER

import sys

def min_ads(n, k, durations):
    durations.sort()  # Sort videos in ascending order
    ads = 0
    time_elapsed = 0
    video_count = 0

    for d in durations:
        video_count += 1
        time_elapsed += d

        if video_count == 3 or time_elapsed >= k:
            ads += 1  # Trigger ad
            video_count = 0  # Reset counter
            time_elapsed = 0  # Reset watch time

    return ads

# Read number of test cases
t = int(input().strip())

for _ in range(t):
    n, k = map(int, input().strip().split())  # Read n and k
    durations = list(map(int, input().strip().split()))  # Read video durations
    print(min_ads(n, k, durations))  # Output the minimum ads needed



