# import os
# import subprocess
#
# def execute_command(command):
#     try:
#         result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
#         return result.stdout, result.stderr
#     except Exception as e:
#         return None, str(e)
#
# def execute_command_realtime(command):
#     try:
#         process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
#         while True:
#             line = process.stdout.readline()
#             if line == '' and process.poll() is not None:
#                 break
#             print(line.strip())
#     except Exception as e:
#         return str(e)
#
# def count_files_in_directory(directory):
#     total_files = 0
#     for root, _, files in os.walk(directory):
#         total_files += len(files)
#     return total_files
#
#
#
# if __name__ == "__main__":
#     # directory_path = "D:/"  # 替换为要遍历的目录路径
#     # print(count_files_in_directory(directory_path))
#
#     # cmd = ".\\engine\\clamav\\clamscan.exe .\\virus\\test\\"  # 替换为你要执行的终端命令
#     # stdout, stderr = execute_command(cmd)
#     # if stdout:
#     #     print("Standard Output:")
#     #     print(stdout)
#     #
#     # if stderr:
#     #     print("Standard Error:")
#     #     print(stderr)
#
#     cmd = ".\\engine\\clamav\\clamscan.exe .\\virus\\test\\"  # 替换为你要执行的终端命令
#     execute_command_realtime(cmd)




import threading
import subprocess
import time

class ScanApp:
    def __init__(self):
        self.running = True
        self.process = None

        self.thread_FilePrint = threading.Thread(target=self.run_scan)
        self.thread_FilePrint.start()

    def run_scan(self):
        cmd = ".\\engine\\clamav\\clamscan.exe .\\virus\\test"
        try:
            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
            while self.running:
                line = self.process.stdout.readline()
                if line == '' and self.process.poll() is not None:
                    break
                print(line.strip())

        except Exception as e:
            print(str(e))

    def terminate_threads(self):
        self.running = False  # 停止子线程
        if self.thread_FilePrint.is_alive():
            self.thread_FilePrint.join()
        if self.process:
            self.process.terminate()  # 终止子进程

if __name__ == "__main__":
    app = ScanApp()

    i=1
    # 在某个条件下终止线程和进程
    while(i<=5):
        print(i)
        time.sleep(1)
        i = i + 1
    print("begin")
    app.terminate_threads()
    print("end")
    print("begin2")
    # 等待子线程结束
    app.thread_FilePrint.join()
    print("end2")