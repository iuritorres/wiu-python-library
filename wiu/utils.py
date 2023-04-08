# Message functions
class Message:

    def send_success(success_msg: str):
        print(f'\033[1;32m[WIU SUCCESS]\033[0m \033[32m{success_msg}!\033[0m')

    def send_warning(warning_msg: str):
        print(f'\033[1;33m[WIU WARNING]\033[0m \033[33m{warning_msg}!\033[0m')

    def send_error(error_msg: str):
        print(f'\033[1;31m[WIU ERROR]\033[0m \033[31m{error_msg}!\033[0m')
