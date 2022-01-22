from src.Functions.Miscellaneous import *

def writeLogs(class_: str, message: str):
    prev_logs = ""

    with open("src\\Main\\logs.logs", "r") as read:
        prev_logs += read.read()

    with open("src\\Main\\logs.logs", "r") as write:
        prev_logs += f"[{getTime()}][{class_}] {message}"