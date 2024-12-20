import yaml
import json
import toml
import configparser
from pathlib import Path
from typing import Any, Dict

class ConversionError(Exception):
    """转换错误的自定义异常类"""
    pass

class BaseConverter:
    """转换器基类"""
    @staticmethod
    def load(content: str) -> Dict[str, Any]:
        raise NotImplementedError
    
    @staticmethod
    def dump(data: Dict[str, Any]) -> str:
        raise NotImplementedError

class YAMLConverter(BaseConverter):
    @staticmethod
    def load(content: str) -> Dict[str, Any]:
        try:
            return yaml.safe_load(content)
        except Exception as e:
            raise ConversionError(f"YAML解析错误: {str(e)}")
    
    @staticmethod
    def dump(data: Dict[str, Any]) -> str:
        try:
            return yaml.dump(data, allow_unicode=True, sort_keys=False)
        except Exception as e:
            raise ConversionError(f"YAML导出错误: {str(e)}")

class JSONConverter(BaseConverter):
    @staticmethod
    def load(content: str) -> Dict[str, Any]:
        try:
            return json.loads(content)
        except Exception as e:
            raise ConversionError(f"JSON解析错误: {str(e)}")
    
    @staticmethod
    def dump(data: Dict[str, Any]) -> str:
        try:
            return json.dumps(data, ensure_ascii=False, indent=2)
        except Exception as e:
            raise ConversionError(f"JSON导出错误: {str(e)}")

class TOMLConverter(BaseConverter):
    @staticmethod
    def load(content: str) -> Dict[str, Any]:
        try:
            return toml.loads(content)
        except Exception as e:
            raise ConversionError(f"TOML解析错误: {str(e)}")
    
    @staticmethod
    def dump(data: Dict[str, Any]) -> str:
        try:
            return toml.dumps(data)
        except Exception as e:
            raise ConversionError(f"TOML导出错误: {str(e)}")

class INIConverter(BaseConverter):
    @staticmethod
    def load(content: str) -> Dict[str, Any]:
        try:
            config = configparser.ConfigParser()
            config.read_string(content)
            return {section: dict(config[section]) for section in config.sections()}
        except Exception as e:
            raise ConversionError(f"INI解析错误: {str(e)}")
    
    @staticmethod
    def dump(data: Dict[str, Any]) -> str:
        try:
            config = configparser.ConfigParser()
            for section, values in data.items():
                config[section] = {str(k): str(v) for k, v in values.items()}
            output = []
            config.write(output)
            return ''.join(output)
        except Exception as e:
            raise ConversionError(f"INI导出错误: {str(e)}")

CONVERTERS = {
    'yaml': YAMLConverter,
    'yml': YAMLConverter,
    'json': JSONConverter,
    'toml': TOMLConverter,
    'ini': INIConverter,
}

EXTENSIONS = {
    'yaml': '.yaml',
    'yml': '.yml',
    'json': '.json',
    'toml': '.toml',
    'ini': '.ini',
} 