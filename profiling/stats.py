import pstats

p_stats = pstats.Stats('profile.stats')
p_stats.sort_stats("cumulative")

# 输出累计时间报告
p_stats.print_stats()

# 输出调用者信息
p_stats.print_callers()

# 输出哪个函数调用了哪个函数
p_stats.print_callees()