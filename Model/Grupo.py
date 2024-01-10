from Model.Login import *

class Grupo(Login):
    def __init__(self, user, headless=False) -> None:
        super().__init__(user, headless)
        self.url = "https://www.facebook.com/groups/joins"
        self.grupos = []

        self.get_groups()
        print(len(self.grupos))
        pausa(3.6,5.5)


    def get_groups(self):
        self.driver.get(self.url)
        try:
            span = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xjkvuk6.x1cnzs8  span.x1lliihq.x6ikm8r.x10wlt62.x1n2onr6.x1j85h84")))[-1]
            n_group = extraer_numeros(span.text)
        except TimeoutError:
            print('error')
        try:

            pausa(0.4,0.8)
            divs = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x8gbvx8.x78zum5.x1q0g3np.x1a02dak.x1nhvcw1.x1rdy4ex.xcud41i.x4vbgl9.x139jcc6")))[1]
            groups = divs.find_elements(By.CSS_SELECTOR,'div.x9f619.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xs83m0k.x150jy0e.x1e558r4.xjkvuk6.x1iorvi4.xnpuxes')
 
            aux = 0
            while n_group> len(groups):
                current_scroll = aux
                try:
                    divs = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x8gbvx8.x78zum5.x1q0g3np.x1a02dak.x1nhvcw1.x1rdy4ex.xcud41i.x4vbgl9.x139jcc6")))[1]
                    groups = divs.find_elements(By.CSS_SELECTOR,'div.x9f619.x78zum5.x1r8uery.xdt5ytf.x1iyjqo2.xs83m0k.x150jy0e.x1e558r4.xjkvuk6.x1iorvi4.xnpuxes')
                except TimeoutException:
                    print("error")
                # Desplaza la página hacia abajo en la cantidad definida por current_scroll

                for i in range(100):
                    self.driver.execute_script(f"window.scrollTo(0, {current_scroll})")
                    pausa(0,0.01)
                    current_scroll += uniform(13.04,14.70)
 
                pausa(0.4,0.5)
                tiempo = uniform(0.3,1.7)

                # Espera un momento para que se cargue más contenido dentro del div de comentarios
                self.driver.implicitly_wait(tiempo) # Ajusta el tiempo según sea necesario
                aux = current_scroll
 
        except TimeoutException:
            print("error")

        try:
            links = divs.find_elements(By.XPATH,"//div[@class='x9f619 x78zum5 x1r8uery xdt5ytf x1iyjqo2 xs83m0k x150jy0e x1e558r4 xjkvuk6 x1iorvi4 xnpuxes']//a[not(child::*)]")

            pattern = re.compile(r'\b(tigre|el tigre|el tigrito|tigrito)\b', re.IGNORECASE)
            for a in links:
                grupo = {}
                if pattern.search(a.text):
                    grupo ={
                        "nombre": a.text,
                        "url":a.get_attribute("href")
                    }
                    self.grupos.append(grupo)
                    
        except TimeoutException:
            print("error")
