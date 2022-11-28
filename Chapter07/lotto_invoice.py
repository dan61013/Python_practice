from prize import exlotto, exreciept

# 樂透開獎
nums = exlotto.lotto(48, 7)
snums = sorted(nums)

print(snums)

# 統一發票開獎
s = exreciept.reciept()

print(s)