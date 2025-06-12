try:
    # action risquée
except Exception as e:
    from modules import error_handler
    error_handler.handle_error("Chargement Bluetooth", e)
