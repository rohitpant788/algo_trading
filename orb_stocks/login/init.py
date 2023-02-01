import helper


#Login in kite browser
def launch_kite_app():
    helper.login_kite_in_browser()


def close_kite_browser():
    helper.get_driver().quit()
