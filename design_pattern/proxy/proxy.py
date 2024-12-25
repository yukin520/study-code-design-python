
from abc import ABC, abstractmethod
import time


class APICaller(ABC):
    @abstractmethod
    def request(self):
        pass


class RealAPICaller(APICaller):
    def __init__(self, url) -> None:
        self._url = url

        # 非常に時間のかかるコンストラクタを想定
        time.sleep(3)
    
    def request(self):
        print("APIを呼び出す")
        return
    

class RealAPICallerProxy(APICaller):
    def __init__(self, url) -> None:
        self._url = url

    def _check_access(self):
        # チェックを行うような処理をカスタマイズして挿入することを想定
        print("チェックに成功しました")
        return True
    
    def _write_log(self):
        print("ログを吐き出しました")

    def request(self):
        if self._check_access():
            # オリジナルのrequest処理の前後で別の処理を追加する
            caller = RealAPICaller(self._url)
            caller.request()
            self._write_log()


# proxyパターンを使用せずに利用する
caller = RealAPICaller("http.example.com")
caller.request()

# proxyパターンを使用の上、利用する
proxy_caller = RealAPICallerProxy("http.example.com")
proxy_caller.request()



