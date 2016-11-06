from flask_wtf import Form
from wtforms.fields import RadioField
from wtforms.validators import Required

class PaymentSettingsForm(Form):
    payment_system = RadioField('Choose payment system', [Required()], 
        choices=[('PayPal', 'PayPal'), ('Privat24', 'privat24'), ('Liqpay', 'Liqpay')], default='PayPal')
    
