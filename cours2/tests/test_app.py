def test_create_app_import():
    # simple smoke test: importing and creating app should work
    from app import create_app
    app = create_app()
    assert app is not None
