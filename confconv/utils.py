from pathlib import Path
from typing import Tuple

def get_file_format(file_path: str) -> str:
    """获取文件格式"""
    return Path(file_path).suffix.lower()[1:]

def generate_output_path(input_path: str, target_format: str) -> str:
    """生成输出文件路径"""
    from .converters import EXTENSIONS
    input_path = Path(input_path)
    return str(input_path.with_suffix(EXTENSIONS[target_format]))

def read_file(file_path: str) -> Tuple[str, str]:
    """读取文件内容和格式"""
    content = Path(file_path).read_text(encoding='utf-8')
    format = get_file_format(file_path)
    return content, format 