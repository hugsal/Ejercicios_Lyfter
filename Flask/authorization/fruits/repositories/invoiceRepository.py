from entities.invoiceEntity import Invoice
from sqlalchemy import select


class InvoiceRepository:
    @staticmethod
    def format_invoice(invoice):
        return {
            "id": invoice.id,
            "total_amount": invoice.total_amount,
            "purchase_date": invoice.purchase_date.strftime("%d/%m/%Y"),
        }

    @staticmethod
    def create_invoice(db, user_id, total_amount):
        new_invoice = Invoice(total_amount=total_amount, fk_user_id=user_id)
        db.add(new_invoice)
        db.commit()
        db.refresh(new_invoice)
        return InvoiceRepository.format_invoice(new_invoice)

    @staticmethod
    def get_invoice_by_user_id(db, user_id):
        stm = select(Invoice).where(Invoice.fk_user_id == user_id)
        return list(map(InvoiceRepository.format_invoice, db.scalars(stm).all()))

    @staticmethod
    def update_total_amount(db, invoice_id, amount):
        invoice = db.get(Invoice, invoice_id)
        if invoice:
            if invoice_id is not None:
                invoice.total_amount = amount
            db.commit()
            db.refresh(invoice)
        return InvoiceRepository.format_invoice(invoice)
