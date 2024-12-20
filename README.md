# confconv
Configuration Converter


## 支持的格式

- YAML (.yaml, .yml)
- JSON (.json)
- TOML (.toml)
- INI (.ini)

## 安装

需要先安装Poetry

```
# Windows
# powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# scoop
scoop install poetry

# 或用pip
pip install poetry

# 添加到系统环境变量（PowerShell）
$Env:Path += ";$env:APPDATA\Python\Scripts"
```
```
# Linux & MacOS
# 使用curl
curl -sSL https://install.python-poetry.org | python3 -

# 使用pip
pip3 install poetry

# 添加到环境变量（bash/zsh）
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # 如果使用 bash
# 或
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc   # 如果使用 zsh
```

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



