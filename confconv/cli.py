import click
from pathlib import Path
from typing import List
from .converters import CONVERTERS, ConversionError
from .utils import read_file, generate_output_path

@click.group()
def cli():
    """配置文件格式转换工具"""
    pass

def convert_file(input_path: str, target_format: str) -> None:
    """转换单个文件"""
    try:
        # 读取源文件内容和格式
        content, source_format = read_file(input_path)
        
        # 检查格式支持
        if source_format not in CONVERTERS:
            raise click.ClickException(f"不支持的源文件格式: {source_format}")
        if target_format not in CONVERTERS:
            raise click.ClickException(f"不支持的目标格式: {target_format}")
        
        # 如果源格式和目标格式相同，跳过转换
        if source_format == target_format:
            click.echo(f"跳过相同格式文件: {input_path}")
            return
            
        # 使用源格式转换器加载数据
        data = CONVERTERS[source_format].load(content)
        
        # 使用目标格式转换器导出数据
        result = CONVERTERS[target_format].dump(data)
        
        # 生成输出文件路径
        output_path = generate_output_path(input_path, target_format)
        
        # 检查是否会覆盖源文件
        if Path(output_path) == Path(input_path):
            raise click.ClickException(f"无法覆盖源文件: {input_path}")
        
        # 保存转换结果
        Path(output_path).write_text(result, encoding='utf-8')
        click.echo(f"已转换: {input_path} -> {output_path}")
        
    except ConversionError as e:
        raise click.ClickException(str(e))
    except Exception as e:
        raise click.ClickException(f"转换失败: {str(e)}")

def create_converter_command(target_format: str):
    """创建转换命令"""
    @cli.command(name=f'to-{target_format}')
    @click.argument('input_files', nargs=-1, type=click.Path(exists=True), required=True)
    @click.option('--force', '-f', is_flag=True, help='强制覆盖已存在的目标文件')
    @click.option('--quiet', '-q', is_flag=True, help='安静模式，不显示转换信息')
    def converter(input_files: List[str], force: bool, quiet: bool):
        """转换为指定格式"""
        for input_file in input_files:
            try:
                # 检查目标文件是否存在
                output_path = generate_output_path(input_file, target_format)
                if Path(output_path).exists() and not force:
                    if not quiet:
                        click.echo(f"目标文件已存在，跳过: {output_path}")
                    continue
                
                convert_file(input_file, target_format)
            except click.ClickException as e:
                if not quiet:
                    click.echo(f"错误: {str(e)}", err=True)
            except Exception as e:
                if not quiet:
                    click.echo(f"未知错误: {str(e)}", err=True)
    return converter

# 为每种支持的格式创建命令
for format_name in CONVERTERS.keys():
    create_converter_command(format_name)

if __name__ == '__main__':
    cli() 