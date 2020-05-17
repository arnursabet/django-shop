from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from utils import upload

class Battery(models.Model):
  POLARITIES = (
    ('П', 'Прямая'),
    ('О', 'Обратная'),
    ('ПО', 'Прямая/Обратная'),
    ('ПиО', 'Прямая и Обратная'),
  )
  SIZES = (
    ('175х175х190','175х175х190'),
    ('187х127х227','187х127х227'),
    ('207х175х175','207х175х175'),
    ('207х175х190','207х175х190'),
    ('232х173х190','232х173х190'),
    ('232х173х225','232х173х225'),
    ('238х129х227','238х129х227'),
    ('242х175х175','242х175х175'),
    ('242х175х190','242х175х190'),
    ('261х175х220','261х175х220'),
    ('272х175х175','272х175х175'),
    ('278х175х190','278х175х190'),
    ('315х175х175','315х175х175'),
    ('353х175х190','353х175х190'),
    ('390х175х190','390х175х190'),
    ('513х189х223','513х189х223'),
    ('518х240х242','518х240х242'),
  )
 
  battery_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  capacity = models.IntegerField()
  voltage = models.IntegerField()
  current = models.IntegerField()
  polarity = models.CharField(max_length=20, choices=POLARITIES)
  size = models.CharField(max_length=15, choices=SIZES, default='none')
  price = models.IntegerField()
  image = models.ImageField(upload_to=upload.battery_upload, max_length=100, null=True)
  
  def __str__(self):
    return self.name

class Order(models.Model):
  order_id = models.AutoField(primary_key=True)
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
  phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
  email = models.EmailField(max_length = 254) 
  comments = models.CharField(max_length=200, default="-")
  date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
    return self.fname + " " + self.lname



