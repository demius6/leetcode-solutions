class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        balance = 100
        if purchaseAmount % 10 < 5:
            return balance - (purchaseAmount//10 * 10)
        else:
            return balance - ((purchaseAmount//10+1) * 10)