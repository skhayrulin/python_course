from typing import Dict, List, Any, Tuple


import typing as t

class A:
    pass

def func(arg1: int, arg2: t.ByteString, arg3: t.List[str], arg4: t.Dict[str, t.Any]) -> bool:
    s: A = A()
    return True

