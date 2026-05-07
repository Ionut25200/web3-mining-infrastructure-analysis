def calculate_daily_revenue(hashrate_th, sta_per_th):

  """
  calculates estimated daily revenue in Satoshis.
  Target : 105.75 TH/s @ sta/TH
  """
  revenue = hasrate_th * sat_per_th
  return revenue

my hashrate = 104
efficiency_yield = 7

daily_total = calculated_daily_revenue(my_hashrate, efficiency_yield)
print(f"Current Daily Yield: {daily_total} Satoshis")


