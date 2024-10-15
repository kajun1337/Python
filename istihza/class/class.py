class Araba:
    # Sınıfın bir örneği oluşturulduğunda çalışacak olan yapıcı metod
    def __init__(self, marka, model, yil):
        # self, sınıfın örneğini temsil eder ve bu örneğe ait özellikleri tanımlar
        self.marka = marka  # Arabanın markasını saklar
        self.model = model  # Arabanın modelini saklar
        self.yil = yil      # Arabanın üretim yılını saklar

    # Arabanın bilgilerini yazdıran bir metod
    def bilgileri_goster(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Yıl: {self.yil}")

# Araba sınıfından bir örnek oluşturuyoruz
araba1 = Araba("Toyota", "Corolla", 2020)

# Arabanın bilgilerini gösteren metodu çağırıyoruz
araba1.bilgileri_goster()