"""Application entrypoint for local Flask execution."""

from src.app import create_app

app = create_app()

if __name__ == "__main__":
    # Debug mode is convenient for local course demos.
    app.run(host="0.0.0.0", port=5000, debug=True)
