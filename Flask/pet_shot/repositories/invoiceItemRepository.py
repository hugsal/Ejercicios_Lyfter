from entities.invoiceItemEntity import InvoiceItem


class InvoiceItemRepository:
    @staticmethod
    def create_register(db, quantity, unit_price, subtotal, product_id, invoice_id):
        new_register = InvoiceItem(
            quantity=quantity,
            unit_price=unit_price,
            subtotal=subtotal,
            fk_product_id=product_id,
            fk_invoice_id=invoice_id,
        )
        db.add(new_register)
        db.commit()
        db.refresh(new_register)
        return new_register
