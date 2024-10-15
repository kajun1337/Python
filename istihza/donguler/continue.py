# 'continue' ifadesi döngüdeki mevcut yinelemeyi atlayarak döngünün bir sonraki yinelemesine geçer.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)