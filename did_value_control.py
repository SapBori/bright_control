import re
# import rclpy

class DIDControl:
    def __init__(self):
        self.file_path = "C:/Users/XYZ/Desktop/code/baris-brew-station-v3/script"
        self.ubuntu_path = "/home/baris-brew/BB3_ROS_WS/script"
        self.up_name = "/light_up.sh"
        self.down_name = "/light_down.sh"
        
    def change_setting(self, request, response):
        response = None
        try:
            if request.cmd == 'UP':
                success = self.modify_files(request.cmd, request.value)
            elif request.cmd == 'DOWN':
                suceess = self.modify_files(request.cmd, request.value)

            response = suceess
        except Exception as error:
            print(f"Logging Value : {success}")

        finally:
            return response
        
    def modify_files(self, cmd, value):
        success = False
        try:
            file = self.file_path

            if cmd == "DOWN":
                file+=self.down_name
            elif cmd == "UP":
                file+=self.up_name

            with open(file=file, mode='r', encoding='utf-8') as read_file:
                lines= read_file.readlines()
            new_lines = []
            new_brightness = str(value)
            for line in lines:
                modified_line = re.sub(r"--brightness\s+(\d+(\.\d+)?)", f"--brightness {new_brightness}", line)
                new_lines.append(modified_line)
            with open(file=file, mode='w', encoding='utf-8') as write_file:
                write_file.writelines(new_lines)
            success = True
        except Exception as error:
            success= False
            print(f"Open File Error Or R/W ERROR")
        finally:
            return success


def main():
    did = DIDControl()
    did.modify_files("UP",0.7)
    did.modify_files("DOWN",0.25)


if __name__ == "__main__":
    main()