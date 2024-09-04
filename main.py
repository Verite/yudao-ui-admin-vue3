import logging

import webview

logging.basicConfig(filename='error.log')


def on_closed():
    print("窗口已关闭")
# 打包命令
# pyinstaller --onefile --add-data "./web/:./web/" --console  main.py
if __name__ == '__main__':
    # 创建一个窗口并加载 HTML 文件
    window = webview.create_window('黑神话-悟空', 'web/index.html', width=1280, height=920, resizable=True)
    webview.start()
