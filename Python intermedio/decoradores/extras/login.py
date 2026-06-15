user_logged_in = False


def requires_login(func):
    def wrapper():
        if not user_logged_in:
            raise PermissionError("Usuario no autenticado")

        func()

    return wrapper


@requires_login
def view_profile():
    print("Mostrando perfil del usuario")


def main():
    try:
        view_profile()
    except Exception as ex:
        print(ex)


main()
