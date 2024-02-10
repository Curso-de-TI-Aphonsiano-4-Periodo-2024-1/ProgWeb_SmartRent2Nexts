
class Log:
    @staticmethod
    def informacao(msg):
        print(f"(!) - {msg}")

    @staticmethod
    def alerta(msg):
        print(f"(@) - {msg}")

    @staticmethod
    def error(msg):
        print(f"(#) - {msg}")
