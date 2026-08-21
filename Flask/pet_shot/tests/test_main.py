import unittest
from unittest.mock import patch, MagicMock
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, Forbidden
from flask import g

import main
from main import (
    app,
    handle_http_exception,
    generate_tokens,
    get_db,
    close_db,
    sigin,
    login,
    me,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
    get_products,
    get_product_by_id,
    create_product,
    update_product,
    delete_product,
    get_carts,
    get_active_cart,
    add_to_cart,
    remove_from_cart,
    create_sale,
    get_invoices,
    get_invoice_by_id as main_get_invoice_by_id,
    refund_invoice,
)
from repositories.cartRepository import CartRepository
from repositories.invoiceRepository import InvoiceRepository


class TestMainHelperMethods(unittest.TestCase):


    def test_handle_http_exception(self):
        ex = BadRequest("Error de prueba")
        response, status_code = handle_http_exception(ex)
        self.assertEqual(status_code, 400)
        self.assertEqual(response, {"message": "Error de prueba"})

    @patch("main.jwt_manager")
    def test_generate_tokens(self, mock_jwt_manager):
        mock_jwt_manager.encode.side_effect = ["access_token_123", "refresh_token_456"]

        access_token, refresh_token = generate_tokens("user123", "admin")

        self.assertEqual(access_token, "access_token_123")
        self.assertEqual(refresh_token, "refresh_token_456")
        self.assertEqual(mock_jwt_manager.encode.call_count, 2)

    def test_get_db_creates_and_reuses_session(self):
        with app.app_context():
            with patch("main.SessionLocal") as mock_session_local:
                mock_db = MagicMock()
                mock_session_local.return_value = mock_db

                db1 = get_db()
                self.assertEqual(db1, mock_db)
                self.assertIn("db", g)

                db2 = get_db()
                self.assertEqual(db2, mock_db)
                mock_session_local.assert_called_once()

    def test_close_db(self):
        with app.app_context():
            mock_db = MagicMock()
            g.db = mock_db

            close_db()

            mock_db.close.assert_called_once()
            self.assertNotIn("db", g)


class TestUserMethods(unittest.TestCase):

    def setUp(self):
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.auth_headers = {"Authorization": "Bearer mock_token"}

    def tearDown(self):
        self.app_ctx.pop()

    @patch("main.generate_tokens")
    @patch("main.UserRepository")
    @patch("main.validate_user_data")
    @patch("main.get_db")
    def test_sigin_success(self, mock_get_db, mock_val_user, mock_user_repo, mock_gen_tokens):
        mock_user_repo.get_user_by_user_name.return_value = None
        mock_user_repo.get_user_by_email.return_value = None
        mock_user_repo.create_user.return_value = {"id": "u1", "role": "client", "name": "Juan"}
        mock_gen_tokens.return_value = ("acc_token", "ref_token")

        with app.test_request_context(json={
            "name": "Juan",
            "email": "juan@test.com",
            "userName": "juanp",
            "password": "123"
        }):
            res, code = sigin()
            self.assertEqual(code, 201)
            self.assertEqual(res["access_token"], "acc_token")
            self.assertEqual(res["user"]["id"], "u1")

    @patch("main.UserRepository")
    @patch("main.validate_user_data")
    @patch("main.get_db")
    def test_sigin_existing_username(self, mock_get_db, mock_val_user, mock_user_repo):
        mock_user_repo.get_user_by_user_name.return_value = {"id": "existing"}

        with app.test_request_context(json={"userName": "juanp", "email": "juan@test.com"}):
            with self.assertRaises(BadRequest):
                sigin()

    @patch("main.UserRepository")
    @patch("main.validate_user_data")
    @patch("main.get_db")
    def test_sigin_existing_email(self, mock_get_db, mock_val_user, mock_user_repo):
        mock_user_repo.get_user_by_user_name.return_value = None
        mock_user_repo.get_user_by_email.return_value = {"id": "existing"}

        with app.test_request_context(json={"userName": "juanp", "email": "juan@test.com"}):
            with self.assertRaises(BadRequest):
                sigin()

    @patch("main.generate_tokens")
    @patch("main.UserRepository")
    @patch("main.validate_login_data")
    @patch("main.get_db")
    def test_login_success(self, mock_get_db, mock_val_login, mock_user_repo, mock_gen_tokens):
        mock_user_repo.get_user_by_user_name.return_value = {
            "id": "u1", "role": "client", "password": "123"
        }
        mock_gen_tokens.return_value = ("acc_token", "ref_token")

        with app.test_request_context(json={"userName": "juanp", "password": "123"}):
            res, code = login()
            self.assertEqual(code, 200)
            self.assertEqual(res["access_token"], "acc_token")

    @patch("main.UserRepository")
    @patch("main.validate_login_data")
    @patch("main.get_db")
    def test_login_invalid_password(self, mock_get_db, mock_val_login, mock_user_repo):
        mock_user_repo.get_user_by_user_name.return_value = {
            "id": "u1", "password": "wrong_password"
        }

        with app.test_request_context(json={"userName": "juanp", "password": "123"}):
            with self.assertRaises(Unauthorized):
                login()

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.get_db")
    def test_me_success(self, mock_get_db, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_user_repo.get_user_by_id.return_value = {"id": "u1", "name": "Juan"}

        with app.test_request_context(headers=self.auth_headers):
            res, code = me()
            self.assertEqual(code, 200)
            self.assertEqual(res["user"]["name"], "Juan")

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.get_db")
    def test_me_user_not_found(self, mock_get_db, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u99", "role": "client"}
        mock_user_repo.get_user_by_id.return_value = None

        with app.test_request_context(headers=self.auth_headers):
            with self.assertRaises(NotFound):
                me()

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.get_db")
    def test_get_users(self, mock_get_db, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_user_repo.get_users.return_value = [{"id": "u1"}, {"id": "u2"}]

        with app.test_request_context(headers=self.auth_headers):
            res, code = get_users()
            self.assertEqual(code, 200)
            self.assertEqual(len(res["users"]), 2)

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.get_db")
    def test_get_user_by_id_success(self, mock_get_db, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_user_repo.get_user_by_id.return_value = {"id": "u1"}

        with app.test_request_context(headers=self.auth_headers):
            res, code = get_user_by_id("u1")
            self.assertEqual(code, 200)
            self.assertEqual(res["user"]["id"], "u1")

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.get_db")
    def test_get_user_by_id_not_found(self, mock_get_db, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_user_repo.get_user_by_id.return_value = None

        with app.test_request_context(headers=self.auth_headers):
            with self.assertRaises(NotFound):
                get_user_by_id("u99")

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.validate_user_data")
    @patch("main.get_db")
    def test_update_user_success(self, mock_get_db, mock_val_user, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_user_repo.get_user_by_id.return_value = {"id": "u1", "userName": "old", "email": "old@test.com"}
        mock_user_repo.get_user_by_user_name.return_value = None
        mock_user_repo.get_user_by_email.return_value = None
        mock_user_repo.update_user.return_value = {"id": "u1", "userName": "new"}

        with app.test_request_context(
            json={"name": "New", "email": "new@test.com", "userName": "new", "role": "admin"},
            headers=self.auth_headers
        ):
            res, code = update_user("u1")
            self.assertEqual(code, 200)
            self.assertEqual(res["user"]["userName"], "new")

    @patch("validateRoles.jwt_manager")
    @patch("main.UserRepository")
    @patch("main.get_db")
    def test_delete_user_success(self, mock_get_db, mock_user_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_user_repo.get_user_by_id.return_value = {"id": "u1"}

        with app.test_request_context(headers=self.auth_headers):
            res, code = delete_user("u1")
            self.assertEqual(code, 200)
            mock_user_repo.delete_user.assert_called_once_with(mock_get_db.return_value, "u1")


class TestProductMethods(unittest.TestCase):

    def setUp(self):
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.auth_headers = {"Authorization": "Bearer mock_token"}

    def tearDown(self):
        self.app_ctx.pop()

    @patch("validateRoles.jwt_manager")
    @patch("main.cache_manager")
    def test_get_products_cached(self, mock_cache, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_cache.get.return_value = [{"id": "p1"}]

        with app.test_request_context(headers=self.auth_headers):
            res, code = get_products()
            self.assertEqual(code, 200)
            self.assertTrue(res["cached"])
            self.assertEqual(len(res["products"]), 1)

    @patch("validateRoles.jwt_manager")
    @patch("main.ProductRepository")
    @patch("main.cache_manager")
    @patch("main.get_db")
    def test_get_products_uncached(self, mock_get_db, mock_cache, mock_prod_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_cache.get.return_value = None
        mock_prod_repo.get_products.return_value = [{"id": "p1"}]

        with app.test_request_context(headers=self.auth_headers):
            res, code = get_products()
            self.assertEqual(code, 200)
            self.assertFalse(res["cached"])
            mock_cache.set.assert_called_once()

    @patch("validateRoles.jwt_manager")
    @patch("main.ProductRepository")
    @patch("main.cache_manager")
    @patch("main.validate_product_data")
    @patch("main.get_db")
    def test_create_product_success(self, mock_get_db, mock_val_prod, mock_cache, mock_prod_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_prod_repo.get_product_by_name.return_value = None
        mock_prod_repo.create_product.return_value = {"id": "p1", "name": "Croquetas"}

        with app.test_request_context(
            json={"name": "Croquetas", "price": 100.0, "stock": 10, "description": "Comida"},
            headers=self.auth_headers
        ):
            res, code = create_product()
            self.assertEqual(code, 201)
            self.assertEqual(res["product"]["id"], "p1")
            mock_cache.invalidate_products.assert_called_once()

    @patch("validateRoles.jwt_manager")
    @patch("main.ProductRepository")
    @patch("main.validate_product_data")
    @patch("main.get_db")
    def test_create_product_already_exists(self, mock_get_db, mock_val_prod, mock_prod_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_prod_repo.get_product_by_name.return_value = {"id": "existing"}

        with app.test_request_context(
            json={"name": "Croquetas", "price": 100.0, "stock": 10},
            headers=self.auth_headers
        ):
            with self.assertRaises(BadRequest):
                create_product()

    @patch("validateRoles.jwt_manager")
    @patch("main.ProductRepository")
    @patch("main.cache_manager")
    @patch("main.get_db")
    def test_delete_product_success(self, mock_get_db, mock_cache, mock_prod_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "admin1", "role": "admin"}
        mock_prod_repo.get_product_by_id.return_value = {"id": "p1"}

        with app.test_request_context(headers=self.auth_headers):
            res, code = delete_product("p1")
            self.assertEqual(code, 200)
            mock_prod_repo.delete_product.assert_called_once()
            mock_cache.invalidate_products.assert_called_once()


class TestCartMethods(unittest.TestCase):

    def setUp(self):
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.auth_headers = {"Authorization": "Bearer mock_token"}

    def tearDown(self):
        self.app_ctx.pop()

    @patch("validateRoles.jwt_manager")
    @patch("main.CartRepository")
    @patch("main.get_db")
    def test_get_carts(self, mock_get_db, mock_cart_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_cart_repo.get_user_carts.return_value = [{"id": "c1"}]

        with app.test_request_context(headers=self.auth_headers):
            res, code = get_carts()
            self.assertEqual(code, 200)
            self.assertEqual(len(res["carts"]), 1)

    @patch("validateRoles.jwt_manager")
    @patch("main.CartRepository")
    @patch("main.ProductRepository")
    @patch("main.get_db")
    def test_add_to_cart_success(self, mock_get_db, mock_prod_repo, mock_cart_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_prod_repo.get_product_by_id.return_value = {"id": "p1"}
        mock_cart_repo.get_or_create_active_cart.return_value = {"id": "c1"}
        mock_cart_repo.add_or_update_item.return_value = {"id": "c1", "items": [{"productId": "p1", "quantity": 2}]}

        with app.test_request_context(json={"productId": "p1", "quantity": 2}, headers=self.auth_headers):
            res, code = add_to_cart()
            self.assertEqual(code, 200)
            self.assertEqual(res["cart"]["id"], "c1")

    @patch("validateRoles.jwt_manager")
    @patch("main.CartRepository")
    @patch("main.get_db")
    def test_remove_from_cart_success(self, mock_get_db, mock_cart_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_cart_repo.get_or_create_active_cart.return_value = {"id": "c1"}
        mock_cart_repo.remove_item.return_value = {"id": "c1", "items": []}

        with app.test_request_context(headers=self.auth_headers):
            res, code = remove_from_cart("p1")
            self.assertEqual(code, 200)
            self.assertEqual(res["cart"]["items"], [])


class TestSalesAndInvoiceMethods(unittest.TestCase):

    def setUp(self):
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.auth_headers = {"Authorization": "Bearer mock_token"}

    def tearDown(self):
        self.app_ctx.pop()

    @patch("validateRoles.jwt_manager")
    @patch("main.cache_manager")
    @patch("main.CartRepository")
    @patch("main.ProductRepository")
    @patch("main.InvoiceRepository")
    @patch("main.InvoiceItemRepository")
    @patch("main.validate_checkout_data")
    @patch("main.get_db")
    def test_create_sale_success(
        self, mock_get_db, mock_val_chk, mock_item_repo, mock_inv_repo, mock_prod_repo, mock_cart_repo, mock_cache, mock_jwt
    ):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_cart_repo.get_or_create_active_cart.return_value = {
            "id": "c1",
            "items": [{"productId": "p1", "quantity": 2}]
        }
        mock_prod = MagicMock()
        mock_prod.id = "p1"
        mock_prod.stock = 10
        mock_prod.price = 50.0
        mock_prod_repo.get_product_entity_by_id.return_value = mock_prod

        mock_inv_repo.create_invoice.return_value = {"id": "inv1"}
        mock_inv_repo.update_total_amount.return_value = {"id": "inv1", "totalAmount": 100.0}

        with app.test_request_context(
            json={"billingAddress": "San Jose", "paymentReference": "REF123"},
            headers=self.auth_headers
        ):
            res, code = create_sale()
            self.assertEqual(code, 201)
            self.assertEqual(res["invoice"]["totalAmount"], 100.0)
            mock_cache.invalidate_products.assert_called_once()
            mock_cache.invalidate_invoices.assert_called_once()

    @patch("validateRoles.jwt_manager")
    @patch("main.CartRepository")
    @patch("main.validate_checkout_data")
    @patch("main.get_db")
    def test_create_sale_empty_cart(self, mock_get_db, mock_val_chk, mock_cart_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_cart_repo.get_or_create_active_cart.return_value = {"id": "c1", "items": []}

        with app.test_request_context(
            json={"billingAddress": "San Jose", "paymentReference": "REF123"},
            headers=self.auth_headers
        ):
            with self.assertRaises(BadRequest):
                create_sale()

    @patch("validateRoles.jwt_manager")
    @patch("main.InvoiceRepository")
    @patch("main.cache_manager")
    def test_refund_invoice_forbidden_user(self, mock_cache, mock_inv_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_inv = MagicMock()
        mock_inv.fk_user_id = "other_user"
        mock_inv_repo.get_invoice_entity_by_id.return_value = mock_inv

        with app.test_request_context(headers=self.auth_headers):
            with self.assertRaises(Forbidden):
                refund_invoice("inv1")

    @patch("validateRoles.jwt_manager")
    @patch("main.InvoiceRepository")
    @patch("main.ProductRepository")
    @patch("main.cache_manager")
    @patch("main.get_db")
    def test_refund_invoice_success(self, mock_get_db, mock_cache, mock_prod_repo, mock_inv_repo, mock_jwt):
        mock_jwt.decode.return_value = {"id": "u1", "role": "client"}
        mock_item = MagicMock()
        mock_item.fk_product_id = "p1"
        mock_item.quantity = 2

        mock_inv = MagicMock()
        mock_inv.fk_user_id = "u1"
        mock_inv.status = "completed"
        mock_inv.items = [mock_item]

        mock_inv_repo.get_invoice_entity_by_id.return_value = mock_inv
        mock_inv_repo.update_status.return_value = {"id": "inv1", "status": "refunded"}

        with app.test_request_context(headers=self.auth_headers):
            res, code = refund_invoice("inv1")
            self.assertEqual(code, 200)
            self.assertEqual(res["invoice"]["status"], "refunded")
            mock_prod_repo.add_stock.assert_called_once_with(mock_get_db.return_value, "p1", 2)


class TestRepositoryMethods(unittest.TestCase):

    def test_format_cart_none(self):
        self.assertIsNone(CartRepository.format_cart(None))

    def test_format_cart_with_items(self):
        mock_product = MagicMock()
        mock_product.id = 10
        mock_product.name = "Croquetas"
        mock_product.price = 25.0

        mock_item = MagicMock()
        mock_item.id = 1
        mock_item.fk_product_id = 10
        mock_item.product = mock_product
        mock_item.quantity = 2

        mock_cart = MagicMock()
        mock_cart.id = 100
        mock_cart.fk_user_id = 5
        mock_cart.status = "active"
        mock_cart.created_at = None
        mock_cart.updated_at = None
        mock_cart.items = [mock_item]

        res = CartRepository.format_cart(mock_cart)
        self.assertEqual(res["id"], 100)
        self.assertEqual(res["totalAmount"], 50.0)
        self.assertEqual(len(res["items"]), 1)
        self.assertEqual(res["items"][0]["product"]["name"], "Croquetas")

    def test_format_invoice_none(self):
        self.assertIsNone(InvoiceRepository.format_invoice(None))

    def test_format_invoice_with_items(self):
        mock_product = MagicMock()
        mock_product.name = "Juguete Perro"

        mock_item = MagicMock()
        mock_item.id = 1
        mock_item.fk_product_id = 20
        mock_item.product = mock_product
        mock_item.quantity = 1
        mock_item.unit_price = 15.0
        mock_item.subtotal = 15.0

        mock_invoice = MagicMock()
        mock_invoice.id = "inv-123"
        mock_invoice.total_amount = 15.0
        mock_invoice.purchase_date = None
        mock_invoice.fk_user_id = 5
        mock_invoice.billing_address = "San Jose"
        mock_invoice.payment_method = "SINPE"
        mock_invoice.payment_reference = "REF999"
        mock_invoice.status = "paid"
        mock_invoice.items = [mock_item]

        res = InvoiceRepository.format_invoice(mock_invoice)
        self.assertEqual(res["id"], "inv-123")
        self.assertEqual(res["items"][0]["productName"], "Juguete Perro")


if __name__ == "__main__":
    unittest.main()

