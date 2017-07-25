class LoginElem():
    usernameInput = driver.find_element_by_id('usernameInput')
    usernameInput.send_keys(username)
    passwordInput = driver.find_element_by_id('passwordInput')
    passwordInput.send_keys(password)
    loginButton = driver.find_element_by_id('loginButton')