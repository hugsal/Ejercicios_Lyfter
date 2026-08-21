from entities.invoiceEntity import Invoice
from entities.invoiceItemEntity import InvoiceItem
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload


class InvoiceRepository:
    @staticmethod
    def format_invoice(invoice):
        if not invoice:
            return None
        formatted_items = []
        for item in invoice.items:
            product = item.product
            formatted_items.append(
                {
                    "id": item.id,
                    "productId": item.fk_product_id,
                    "productName": product.name if product else None,
                    "quantity": item.quantity,
                    "unitPrice": item.unit_price,
                    "subtotal": item.subtotal,
                }
            )

        return {
            "id": invoice.id,
            "totalAmount": invoice.total_amount,
            "purchaseDate": invoice.purchase_date.strftime("%Y-%m-%d %H:%M:%S")
            if invoice.purchase_date
            else None,
            "userId": invoice.fk_user_id,
            "billingAddress": invoice.billing_address,
            "paymentMethod": invoice.payment_method,
            "paymentReference": invoice.payment_reference,
            "status": invoice.status,
            "items": formatted_items,
        }

    @staticmethod
    def create_invoice(
        db, user_id, total_amount, billing_address, payment_method, payment_reference
    ):
        new_invoice = Invoice(
            fk_user_id=user_id,
            total_amount=total_amount,
            billing_address=billing_address,
            payment_method=payment_method,
            payment_reference=payment_reference,
            status="paid",
        )
        db.add(new_invoice)
        db.commit()
        return InvoiceRepository.get_invoice_by_id(db, new_invoice.id)

    @staticmethod
    def get_invoice_by_id(db, invoice_id):
        stmt = (
            select(Invoice)
            .options(selectinload(Invoice.items).joinedload(InvoiceItem.product))
            .where(Invoice.id == str(invoice_id))
        )
        invoice = db.scalar(stmt)
        if not invoice:
            return None
        return InvoiceRepository.format_invoice(invoice)

    @staticmethod
    def get_invoice_entity_by_id(db, invoice_id):
        stmt = (
            select(Invoice)
            .options(selectinload(Invoice.items).joinedload(InvoiceItem.product))
            .where(Invoice.id == str(invoice_id))
        )
        return db.scalar(stmt)

    @staticmethod
    def get_invoices_by_user_id(db, user_id):
        stmt = (
            select(Invoice)
            .options(selectinload(Invoice.items).joinedload(InvoiceItem.product))
            .where(Invoice.fk_user_id == user_id)
            .order_by(Invoice.purchase_date.desc())
        )
        invoices = db.scalars(stmt).unique().all()
        return list(map(InvoiceRepository.format_invoice, invoices))

    @staticmethod
    def get_all_invoices(db):
        stmt = (
            select(Invoice)
            .options(selectinload(Invoice.items).joinedload(InvoiceItem.product))
            .order_by(Invoice.purchase_date.desc())
        )
        invoices = db.scalars(stmt).unique().all()
        return list(map(InvoiceRepository.format_invoice, invoices))

    @staticmethod
    def update_total_amount(db, invoice_id, amount):
        invoice = db.get(Invoice, str(invoice_id))
        if invoice:
            invoice.total_amount = amount
            db.commit()
            return InvoiceRepository.get_invoice_by_id(db, invoice_id)
        return None

    @staticmethod
    def update_status(db, invoice_id, status):
        invoice = db.get(Invoice, str(invoice_id))
        if invoice:
            invoice.status = status
            db.commit()
            return InvoiceRepository.get_invoice_by_id(db, invoice_id)
        return None

