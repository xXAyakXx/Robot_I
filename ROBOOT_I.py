import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#-- CONTROLES --
chrome_opcion = webdriver.ChromeOptions()
chrome_opcion.add_experimental_option("excludeSwitches",['enable-automation']) #ESTA LINEA ELIMINA EL MENSAJE DE QUE CHROME ESTA SIENDO UTILIZADO
chrome_opcion.add_experimental_option("detach",True)#ESTA LINEA EVITA QUE CHROME SE CIERRE AUTOMATICAMENTE
driver = webdriver.Chrome(options=chrome_opcion)
driver.get("https://twitter.com/i/flow/login")
driver.implicitly_wait(5)
#-- FIN DE CONTROL --

#BOTON DE INICIO DE SESION- A TRAVES DE XPATH DE LA PAGINA WEB
sign_in = driver.find_element(By.XPATH,'//html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
sign_in.click()

#TEXT BOX DE NOMBRE DEL USUARIO
usuario = driver.find_element(By.XPATH,"//input[@autocomplete='username']")
usuario.send_keys('xxxxxxxxxx') #USUARIO DEL ROBOT_I

#EN EL BOTON DE SIGUIENTE SE LE PONE -2 POR QUE HAY CUATRO BOTONES
next_btn = driver.find_elements(By.XPATH,"//div[@role='button']")
time.sleep(8)
next_btn[-2].click()

#INGRESO LA CONTRASEÑA DE INPUT
driver.implicitly_wait(8)
contraseña = driver.find_element(By.XPATH,"//input[@autocomplete='current-password']")
contraseña.send_keys('xxxxxxxx') # CONTRASEÑA DEL CORREO ELECTRONICO

#HACIENDO CLIC EN EL BOTONN DE LOG IN SE LE PONE -1 PARA EL ULTIMO BOTON
next_btn = driver.find_elements(By.XPATH,"//div[@role='button']")
time.sleep(8)
next_btn[-1].click()

#REALIZANDO LA BUSQUEDA EN EL INPUT DE BUSQUEDA DE TUITER
BUSQUEDA = "xxxxxxxxxx"
time.sleep(8)
driver.get("https://twitter.com/search?q=" + BUSQUEDA + "&src=typed_query&f=top")

#HACIENDO CLIC EN ME GUSTA
b_megusta = driver.find_elements(By.XPATH,"//div[@data-testid='like']")
time.sleep(4)
b_megusta[0].click()

#HACIENDO CLIC EN RETUIT Y DEJAR COMENTARIO
b_retuit = driver.find_elements(By.XPATH,"//div[@data-testid='retweet']")
time.sleep(4)
b_retuit[0].click()

#EN EL SUB MENU DEL RETUIT ESCOJEMOS DEJAR COMENTARIO "QUOTE"
coment = driver.find_element(By.XPATH,"//a[@role='menuitem']")
time.sleep(4)
coment.click()
time.sleep(8)

#PONIENDO EL COMENTARIO
comentario = driver.find_element(By.XPATH,"//div[contains(@class,'public-DraftStyleDefault-block')]")
comentario.send_keys("hola Mundo :)")
time.sleep(8)
tuitear = driver.find_element(By.XPATH,"//div[@data-testid='tweetButton']")
time.sleep(4)
tuitear.click()
time.sleep(8)