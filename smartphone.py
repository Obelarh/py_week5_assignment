class SmartPhone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    def get_phone_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"
    
class GamingSmartphone(SmartPhone):
    def __init__(self, brand, model, storage, battery_level, gpu_performance):
        super().__init__(brand, model, storage)
        self.gpu_performance = gpu_performance


my_phone = SmartPhone("Apple", "iPhone 14", 128)
gaming_phone = GamingSmartphone("Razer", "Phone 2", 256, 90, "Adreno 640")
print(my_phone.get_phone_info()) 
print(gaming_phone.get_phone_info())
