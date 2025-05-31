import sys
from gunicorn.app.wsgiapp import run

def Run_gunicorn() -> None:
    """
    Function for start server gunicorn 
    for deployment

    Parameters
    ----------
    
    Returns
    -------
    `None`
    """
    sys.argv = [
        "gunicorn",
        "--bind", "0.0.0.0:8013",
        "--workers", "2",
        "RecommenderSystem.__main__:app",
    ]
    run()