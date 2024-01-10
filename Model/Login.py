from Model.Driver import *

class Login(Driver):
    def __init__(self, user, headless=False) -> None:
        super().__init__(user['user'], headless)
        self.FB_USER = user['user']
        self.FB_PASS = user['password']

        login = self.login_facebook()

        pausa(3,5)
        if not login:
            sys.exit()

    def login_facebook(self):
        #abrimos la pagina de facebook
        print("Login facebook desde CERO")
       
        if os.path.isfile(self.COOKIES_FILE):
            # leemos la cookies del archivos
        
            cookies = pickle.load(open(self.COOKIES_FILE, "rb"))

            self.driver.get("https://www.facebook.com/robots.txt")
            # recorremos el objeto cookies y lo añadimos al driver
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://www.facebook.com/")
            try:
                elemento = self.wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "input[type='search']")))
                print("Login por cookies: OK")
                return "OK"
            except TimeoutException:
                print("Error al cargar las coockies")
                return False
        self.driver.get("https://www.facebook.com/")
        try:
            elemento = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        except TimeoutException:
            print("Error al introducir usuario")
            return False
        print("Introduciendo Usuario: OK")
        tecleo_lento(elemento,self.FB_USER)
        
        try:
            elemento = self.wait.until(EC.visibility_of_element_located((By.NAME, "pass")))
        except TimeoutException:
            print("Error al introducir contraseña")
            return False
        print("Introduciendo Contrasena: OK")
        
        tecleo_lento(elemento,self.FB_PASS)
 
        try:
            elemento = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        except TimeoutException:
            print("Error al \"Iniciar Sesion\"")
            return False
        print("Click en \"Iniciar Sesion\": OK")
        pausa(1.7,3)
        elemento.click()
 
        try:
            elemento = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.x78zum5.x1n2onr6.xh8yej3")))
        except TimeoutException:
            return False
        print("Login desde Cero: OK")
        # obtener cockies
        carpeta = "db"
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)
        cookies = self.driver.get_cookies()
        pickle.dump(cookies, open(self.COOKIES_FILE,"wb"))
        print("Cookies guardadas")
        
        return "OK"