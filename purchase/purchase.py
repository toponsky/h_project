import sys

from safari import safari_purchase as sPurchase
from chrome import chrome_purchase as cPurchase


if __name__ == "__main__":
  # sPurchase = sPurchase.SafariPurchase()
  sPurchase = cPurchase.ChromePurchase()
  url = sys.argv[1]
  sPurchase.addToShoppingCard(url)
