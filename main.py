import modules.interface as interface

def main():
    try:
        interface.run_app()
    except Exception as e:
        print(f"[SPYNBOOX] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
