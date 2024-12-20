# confconv
Configuration Converter


## 支持的格式

- YAML (.yaml, .yml)
- JSON (.json)
- TOML (.toml)
- INI (.ini)

## 安装
```
poetry install
poetry build
cd dist
pip install ./confconv-0.1.0-py3-none-any.whl

```

## 使用方法

```
confconv to-json config.yaml # 将生成 config.json
confconv to-yaml config.json # 将生成 config.yaml
confconv to-toml config.json # 将生成 config.toml
confconv to-ini config.yaml # 将生成 config.ini

# 批量转换多个文件
confconv to-json config1.yaml config2.yaml config3.yml
```



