from watchdog.observers import Observer
from watchdog.events import *
import time

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹由 { event.src_path } 移动至 { event.dest_path}")
        else:
            print(f"{now} 文件由 {event.src_path} 移动至 {event.dest_path}")

    def on_created(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹由 { event.src_path } 创建")
        else:
            print(f"{now} 文件由 {event.src_path} 创建")

    def on_deleted(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹由 { event.src_path } 删除")
        else:
            print(f"{now} 文件由 {event.src_path} 删除")

    def on_modified(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory:
            print(f"{ now } 文件夹由 { event.src_path } 修改")
        else:
            print(f"{now} 文件由 {event.src_path} 修改")

if __name__ == "__main__":
    observer = Observer()
    path = r"d:\test"
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path, True) # True表示递归子目录
    print(f"监控目录 {path}")
    observer.start()
    observer.join()