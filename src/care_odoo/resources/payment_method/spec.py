from pydantic import BaseModel


class PaymentMethodData(BaseModel):
    id: int
    name: str
    code: str


class SetOdooPaymentMethodRequest(BaseModel):
    odoo_payment_method_id: int | None = None
