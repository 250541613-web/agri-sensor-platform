from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tarla Adı")
    location = models.CharField(max_length=255, verbose_name="Konum Bilgisi", blank=True, null=True)
    area_size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Yüzölçümü (Dönüm)")
    crop_type = models.CharField(max_length=100, verbose_name="Ekili Ürün")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return f"{self.name} - {self.crop_type}"

    class Meta:
        verbose_name = "Tarla"
        verbose_name_plural = "Tarlalar"

class SensorData(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="sensor_data", verbose_name="Tarla")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Ölçüm Zamanı")
    humidity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Nem (%)")
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Sıcaklık (°C)")
    soil_ph = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Toprak pH")
    light_intensity = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Işık Yoğunluğu (Lux)")

    def __str__(self):
        return f"{self.field.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Sensör Verisi"
        verbose_name_plural = "Sensör Verileri"

class IrrigationLog(models.Model):
    ACTION_CHOICES = [
        ('IRRIGATION', 'Sulama'),
        ('FERTILIZATION', 'Gübreleme'),
    ]

    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="irrigation_logs", verbose_name="Tarla")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="İşlem Zamanı")
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES, verbose_name="İşlem Tipi")
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Miktar (Litre/Kg)")
    notes = models.TextField(blank=True, null=True, verbose_name="Notlar")

    def __str__(self):
        return f"{self.field.name} - {self.get_action_type_display()} - {self.timestamp.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Sulama/Gübreleme Kaydı"
        verbose_name_plural = "Sulama/Gübreleme Kayıtları"