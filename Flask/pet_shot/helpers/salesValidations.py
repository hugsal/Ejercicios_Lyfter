from flask import abort


def validate_checkout_data(data):
    if not data:
        abort(400, "No se enviaron datos de compra")

    billing_address = data.get("billingAddress")
    payment_method = data.get("paymentMethod", "SINPE")
    payment_reference = data.get("paymentReference")

    if not billing_address or not str(billing_address).strip():
        abort(400, "La dirección de facturación es obligatoria")

    if not payment_reference or not str(payment_reference).strip():
        abort(400, "El comprobante/referencia de pago (ej. SINPE) es obligatorio")
