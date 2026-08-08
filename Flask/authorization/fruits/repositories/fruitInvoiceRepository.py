from entities.fruitsInvoiceEntity import FruitsInvoice


class FruitsInvoiceRepository:
    @staticmethod
    def create_register(db, quantity, total_amount, fruit_id, invoice_id):
        new_register = FruitsInvoice(
            quantity=quantity,
            total_amount=total_amount,
            fk_fruit_id=fruit_id,
            fk_invoice_id=invoice_id,
        )
        db.add(new_register)
        db.commit()
        db.refresh(new_register)
        return new_register
