import random
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File

class Certificate(models.Model):
    profile_photo = models.ImageField(null=True, blank = True, upload_to = "certificate/")
    certificate_number = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=225)
    role = models.CharField(max_length=225)
    organization = models.CharField(default="Kartexa", max_length=255)
    organizer = models.CharField(max_length=225)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    generated_date = models.DateTimeField(default=timezone.now)
    verification_link= models.URLField(max_length=200, default="demo")
    qr_image = models.ImageField(upload_to='qrcode', blank=True)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.verification_link)
        canvas = Image.new("RGB", (300,300), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_image.save(f'image{random.randint(0,9999)}', File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.certificate_number}"
    

