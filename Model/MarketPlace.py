from Model.Grupo import *

class MarketPlace(Grupo):
    def __init__(self, user, producto, headless=False) -> None:
        super().__init__(user, headless)
        self.titulo,self.descripcion,self.precio ,self.categoria = producto
        self.url = "https://www.facebook.com/marketplace/create/item"

        # self.create_item()

        # pausa(3.2,5.5)

    def create_item(self):
        self.driver.get(self.url)
        try:
            #div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x78zum5.x1iyjqo2
            elemento = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x78zum5.x1iyjqo2")))
            elemento.click()
            img = None
            while True:
                try:
                    img = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"img.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.x5yr21d.xl1xv1r.x10l6tqk.x17qophe.x13vifvy.xh8yej3.x1v9uhfc")))
                except:
                    pass
                if img:
                    break
                pausa()
        except TimeoutException:
            print("Error")
        try:
            inputs = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input.x1i10hfl.xggy1nq.x1s07b3s.x1kdt53j.x1a2a7pz.xjbqb8w.x76ihet.xwmqs3e.x112ta8.xxxdfa6.x9f619.xzsf02u.x1uxerd5.x1fcty0u.x132q4wb.x1a8lsjc.x1pi30zi.x1swvt13.x9desvi.xh8yej3.x15h3p50.x10emqs4")))
            contenedor = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x78zum5.xdt5ytf.x193iq5w.xeuugli.x2lah0s.x1t2pt76.x1xzczws.x1cvmir6.x1vjfegm.xwn1f64 > div > div")))
            # haciendo scroll hasta el input titulo
            y = inputs[0].location['y']
            y = int(y)/2
  
            aux = 0
            self.scrolling_into_container(y,aux,contenedor[1])

        except TimeoutException:
            print("error")
            
        try:
            titulo = inputs[0]
            pausa(0.7,1.2)
            tecleo_lento(titulo,self.titulo)

        except TimeoutException:
            print("error")
        try:
 
            precio = inputs[1]
            pausa(0.5,1.7)
            tecleo_lento(precio,str(self.precio))

        except TimeoutException:
            print("error")
        try:
            pausa(1.5,2)
            # click en input categoria
            elemento = self.wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, "div.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj")))
            elemento[0].click()
            divs_categoria = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x1iz1s3.x1rife3k.x2ewi1q div span")))

            for div in divs_categoria:
                span = div
                if self.categoria.strip() == span.text.strip().lower():
                    break
            
        except TimeoutException:
            print("Error")

        try:
            # selecionando la categoria
            div = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.x1iz1s3.x1rife3k.x2ewi1q")))
 
            y = span.location['y']
            y = int(y)
            if y > 1000:
                y/=2

            aux = 0
            self.scrolling_into_container(y,aux,div)
                    
            span.click()
            pausa(0.2,0.8)
            # haciendo click en input estado
            elemento[1].click()
 
            pausa(0.4,1.2)

            nuevo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.xe8uvvx.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x9f619.x1ypdohk.x78zum5.x1q0g3np.x2lah0s.xnqzcj9.x1gh759c.xdj266r.xat24cr.x1344otq.x1de53dj.xz9dl7a.xsag5q8.x1n2onr6.x16tdsg8.x1ja2u2z")))
            nuevo.click()

        except TimeoutException:
            print("error")
        
        try:
            contenedor = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x78zum5.xdt5ytf.x193iq5w.xeuugli.x2lah0s.x1t2pt76.x1xzczws.x1cvmir6.x1vjfegm.xwn1f64 > div > div")))
         
            textarea =  self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
            y1 = elemento[1].location['y']
 
            y = textarea.location['y']
            aux = y1
            self.scrolling_into_container(y,aux,contenedor[2])
 
            tecleo_lento(textarea,self.descripcion)
        except TimeoutException:
            print("error")
        
        try:
            marcadores = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1lliihq")))

            marcadores = marcadores[1:-2]
            contenedor = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x78zum5.xdt5ytf.x193iq5w.xeuugli.x2lah0s.x1t2pt76.x1xzczws.x1cvmir6.x1vjfegm.xwn1f64 > div > div")))
         
            y1 = textarea.location['y']
            y = marcadores[-1].location['y']
 
            y1+=450
            y+=200
                
            aux = y1
            self.scrolling_into_container(y,aux,contenedor[2])

            for marcador in marcadores:
                pausa()
                marcador.click()
        except TimeoutException:
            print("error")
        
        try:

            pausa(0.4,0.8)
            submit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Siguiente']")))
 
            submit.click()
        except TimeoutException:
            print("error")

        try:
            contenedor = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.x9f619.x1n2onr6.x78zum5.xdt5ytf.x193iq5w.xeuugli.x2lah0s.x1t2pt76.x1xzczws.x1cvmir6.x1vjfegm.xwn1f64 > div > div")))[2]    
            contenedor_grupos = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div > div.x1n2onr6.x1ja2u2z.x9f619.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xz9dl7a")))
            contenedores_titulos = contenedor_grupos.find_elements(By.CSS_SELECTOR,"div.x6s0dn4.x1q0q8m5.x1qhh985.xu3j5b3.xcfux6l.x26u7qi.xm0m39n.x13fuv20.x972fbf.x9f619.x78zum5.x1q0g3np.x1iyjqo2.xs83m0k.x1qughib.xat24cr.x11i5rnm.x1mh8g0r.xdj266r.xeuugli.x18d9i69.x1sxyh0.xurb0ha.xexx8yu.x1n2onr6.x1ja2u2z.x1gg8mnh")
            titulos = [titulo.find_element(By.CSS_SELECTOR,"span > span > span") for titulo in contenedores_titulos]
            titulos = [titulo.text for titulo in titulos]
            coleccion_titulos = []
            grupos = [grupo['nombre'] for grupo in self.grupos]
            for titulo in titulos:
                if titulo in grupos:
                    coleccion_titulos.append(titulo)
            # for titulo in titulos:
            #     for grupo in self.grupos:
            #         if titulo == grupo['nombre']:
            #             coleccion_titulos.append(titulo)
            #             break
            #     continue
            aux = 0
            y = contenedor_grupos.location['y']
            self.scrolling_into_container(y,aux,contenedor)
            cont = 0
            for i in range(0,len(contenedores_titulos)-1,7):

                j = min(i + 7, len(contenedores_titulos)-1)
                for r in range(i,j):
                    if cont>19 or cont > len(self.grupos)-2:
                        break
                    if titulos[r] in coleccion_titulos:
                        try:  
                            cont+=1
                            selector = contenedores_titulos[r].find_element(By.CSS_SELECTOR,'i.x1b0d499.xep6ejk')
                            selector.click()
                            coleccion_titulos.remove(titulos[r])
                        except TimeoutException:
                            print("Error")
                        pausa(0.4,1)

                aux = y
                y = contenedores_titulos[j].location['y']+300
                self.scrolling_into_container(y,aux,contenedor)
                pausa()

            grupos = []
            for grupo in self.grupos:
                if grupo["nombre"] in coleccion_titulos:
                    grupos.append(grupo)
                    # i = self.grupos.index(grupo)
                    # self.grupos.pop(i)
            self.grupos = grupos

        except TimeoutException:
            print("error")

        try:
            submit = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[aria-label='Publicar']")))
            submit.click()
            pausa(15,45)
        except TimeoutException:
            print("error")
