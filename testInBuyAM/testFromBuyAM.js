const { Builder, By, Key, until} = require('selenium-webdriver');
fs = require('fs');
(async function example() {
    let driver = await new Builder().forBrowser('firefox').build();
    await driver.get('https://buy.am/hy/checkout/confirm')
    email = driver.findElement(By.id("email"));
    password = driver.findElement(By.name("password"))

    email.sendKeys("titef81941@moneyzon.com");
    password.sendKeys("123456789");

    element = driver.wait(until.elementLocated(By.className ("register--login-btn btn is--primary is--large"), 2000)).click();
    element = driver.wait(until.elementLocated(By.id ("payment-button"), 2000)).click();

    await driver.sleep(10000);

    iPAN = driver.findElement(By.id("iPAN"))
    iTEXT = driver.findElement(By.id("iTEXT"))
    iCVC = driver.findElement(By.id("iCVC"))

    iPAN.sendKeys("123456789");
    iTEXT.sendKeys("asdasd");
    iCVC.sendKeys("1234");

    driver.wait(until.elementLocated(By.id ("buttonPayment"), 2000)).click();

})();

