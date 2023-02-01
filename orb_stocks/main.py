import kite_automation_config
from login import init as init_login
from prepare import init as prepare_trade

#Step 1 : Login in kite browser
init_login.launch_kite_app()

#Step 2 : Prepare Watch list
prepare_trade.add_stock_to_watchlist()

#Step 3 : Mark high and low of first Candle/ TODO make it range
prepare_trade.fetch_high_low(kite_automation_config.KITE_ORB_CANDLE_DURATION)

#Step 4 : Trade the breakout
prepare_trade.trade_the_breakout()

#Step 4: Testing only
# prepare_trade.place_order("buy",870)
# prepare_trade.place_order("sell",870)

#Step N : Close the open browser
init_login.close_kite_browser()



