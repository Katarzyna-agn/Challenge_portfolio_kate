# Zadanie 1: Konfiguracja oprogramowania.
## Podzadanie 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?
Zdecydowałam się na udział w wyzwaniu Dare IT ponieważ posiadam doświadczenie w testach manualnych i chciałabym poszerzyć swoją wiedzę w zakresie testów automatyzujących.
# Zadanie 2: Selektory.
### Remind password
* //*[@id="__next"]/form/div/div[1]/a
*//*[text()="Remind password"]
//*[contains(@class, "MuiTypography-root MuiLink")]  

### Login
//*[@id="login"]
//*[@name="login"]
//*[@type="text"] --ryzykowne, ale nie ma na stronie logowania innego elementu z tym typem



### Password
//*[@id="password"]
//*[@name="password"]
//*[@type="password"]



### Sign in
//*[text()="Sign in"]
//*[@class="MuiButton-label"]

### Change language
//*[@id="__next"]/form/div/div[2]/div/div

