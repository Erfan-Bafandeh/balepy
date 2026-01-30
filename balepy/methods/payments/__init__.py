from .send_invoice import SendInvoice
from .create_invoice_link import CreateInvoiceLink



class Payments(SendInvoice,
               CreateInvoiceLink):
    pass
