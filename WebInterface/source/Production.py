import sys
from gunicorn.app.wsgiapp import run

def Run_gunicorn() -> None:
    """
        Function for start server gunicorn 
        for deployment
    """
    sys.argv = [
        "gunicorn",
        "--bind", "0.0.0.0:5000",
        "--workers", "2",
        "WebInterface.__main__:app",
    ]
    run()