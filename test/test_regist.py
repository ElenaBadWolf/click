def test_regist(app):
    app.registration.registration_individual()


def test_registration_company(app):
    app.registration.registration_company()


def test_black_list(app):
    app.registration.black_list()


def test_registration_europe(app):
    app.registration.registration_europe()
